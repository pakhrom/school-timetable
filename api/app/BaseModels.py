import datetime
import logging
from http.client import HTTPException
from typing import Optional, Annotated

import bson.errors
from pydantic import BaseModel, field_validator, ValidationError, Field, model_validator, BeforeValidator
from enum import Enum
# import hashlib
from pymongo.synchronous.collection import Collection
from bson import ObjectId

def isValidObjectId(value: str | ObjectId) -> str:
    if not ObjectId.is_valid(value):
        raise ValueError("Invalid ObjectId")
    return str(value)

PyObjectId = Annotated[str, BeforeValidator(isValidObjectId)]

class SubjectBase(BaseModel):
    shortName: str = Field(max_length=10)
    fullName: str = Field(min_length=1, max_length=20)
    optional: bool = False
    groupsIds: list[PyObjectId] = []

class GroupBase(BaseModel):
    subjectId: PyObjectId
    teacherId: PyObjectId
    cabinet: str = Field(min_length=3, max_length=20)
    attendPeriodicity: int = Field(gt=0)

    @classmethod
    def pairGroup(
            cls,
            collection: Collection | list[Collection],
            addId: PyObjectId,
            selectId: PyObjectId | list[PyObjectId],
    ):
        def pairOneElement(
                collection: Collection,
                addId: PyObjectId,
                selectId: PyObjectId,
        ):
            try:
                pairedGroups: list[PyObjectId] = collection.find_one(
                    filter={"_id": ObjectId(selectId)}
                )["groupsIds"]
            except KeyError:
                raise HTTPException(404, f"Subject with id: {selectId} cant be found")

            pairedGroups.append(addId)

            return collection.update_one(
                filter={"_id": ObjectId(selectId)},
                update={"$set": {
                    "groupsIds": pairedGroups,
                    "updateDate": datetime.datetime.now()
                }}
            )

        if isinstance(selectId, list)  and isinstance(collection, list):
            for oneSelectId, oneCollection in zip(selectId, collection):
                pairOneElement(
                    collection=oneCollection,
                    addId=addId,
                    selectId=oneSelectId
                )

        elif isinstance(selectId, str) and isinstance(collection, Collection):
            pairOneElement(
                collection=collection,
                addId=addId,
                selectId=selectId
            )
        else:
            raise TypeError("Pass all lists of elements or single element")

        return 0

    @classmethod
    def unpairGroup(
            cls,
            collection: Collection | list[Collection],
            delId: PyObjectId,
            selectId: PyObjectId | list[PyObjectId],
    ):
        def unpairOneElement(
                collection: Collection,
                delId: PyObjectId,
                selectId: PyObjectId,
        ):
            try:
                pairedGroups: list[PyObjectId] = collection.find_one(
                    filter={"_id": ObjectId(selectId)}
                )["groupsIds"]
            except KeyError:
                raise HTTPException(404, f"Subject with id: {selectId} cant be found")

            pairedGroups.remove(delId)

            return collection.update_one(
                filter={"_id": ObjectId(selectId)},
                update={"$set": {
                    "groupsIds": pairedGroups,
                    "updateDate": datetime.datetime.now()
                }}
            )

        if isinstance(selectId, list)  and isinstance(collection, list):
            for oneSelectId, oneCollection in zip(selectId, collection):
                unpairOneElement(
                    collection=oneCollection,
                    delId=delId,
                    selectId=oneSelectId
                )

        elif isinstance(selectId, str)  and isinstance(collection, Collection):
            unpairOneElement(
                collection=collection,
                delId=delId,
                selectId=selectId
            )
        else:
            raise TypeError("Pass all lists of elements or single element")

        return 0

    def printOut(
            self,
            subjectsCollection: Collection,
            teacherCollection: Collection,
    ):
        try:
            from app.FullModels import SubjectFull, TeacherFull
            return self.model_dump(
                exclude={"subjectId", "teacherId"}
            ) | {
                "subject": SubjectFull(**subjectsCollection.find_one({"_id": ObjectId(self.subjectId)})),
                "teacher": TeacherFull(**teacherCollection.find_one({"_id": ObjectId(self.teacherId)}))
            }
        except TypeError:
            raise HTTPException(422, f"Object {self.__name__} with id: {self.model_fields()['objId']}")

    def verify_dependencies(
            self,
            teachersCollection: Collection,
            subjectsCollection: Collection,
    ) -> bool:
        logger = logging.getLogger("uvicorn.debug")
        if not teachersCollection.find_one({"_id": ObjectId(self.teacherId)}):
            logger.debug("Unable to find teacher")
            return False

        if not subjectsCollection.find_one({"_id": ObjectId(self.subjectId)}):
            logger.debug("unable to find subject")
            return False

        return True

class Gender(str, Enum):
    male = 'male'
    female = 'female'

class FullName(BaseModel):
    first: str = Field(min_length=1, max_length=15)
    last: str = Field(min_length=1, max_length=15)
    middle: str = Field(min_length=1, max_length=15)

class TeacherBase(BaseModel):
    gender: Gender
    fullname: FullName
    groupsIds: list[PyObjectId] = list()

class Replacement(BaseModel):
    lesson: int = Field(gt=0, lt=13)
    reason: Optional[str] = Field(max_length=20)
    oldGroupId: PyObjectId
    newGroupId: Optional[PyObjectId]

    def verify_dependencies(
            self,
            groupsCollection: Collection,
    ) -> bool:
        logger = logging.getLogger("uvicorn.debug")
        DBResponse_oldG = groupsCollection.find_one({"_id": ObjectId(self.oldGroupId)})
        if not DBResponse_oldG:
            logger.debug("Unable to find old group")
            return False
        if self.newGroupId:
            DBResponse_newG = groupsCollection.find_one({"_id": ObjectId(self.newGroupId)})
            if not DBResponse_newG:
                logger.debug("Unable to find new group")
                return False
        return True


class ReplacementsBase(BaseModel):
    date: datetime.datetime
    modifiedGroups: Optional[list[Replacement]] = []
    callScheduleId: Optional[PyObjectId]

    def verify_dependencies(
            self,
            callSchedulesCollection: Collection,
    ) -> bool:
        if self.callScheduleId:
            if not callSchedulesCollection.find_one({"_id": ObjectId(self.callScheduleId)}):
                logger = logging.getLogger("uvicorn.debug")
                logger.debug("Couldn`t find callSchedule object")
                return False
        return True

class TimetableBase(BaseModel):
    className: str = Field(min_length=2, max_length=10)
    groupsIds: list[PyObjectId] = list()
    week: list[Annotated[
        list[Annotated[list[
            PyObjectId  # groupId
        ], Field(min_length=0, max_length=13)]
        ], Field(min_length=6, max_length=7)
    ]]

    @model_validator(mode="after")
    def groups_is_equal(
            self
    ):
        # logger = logging.getLogger("uvicorn.debug")
        uniqueGroups = set()
        for day in self.week:
            for lesson in day:
                uniqueGroups.update(lesson)

        if not uniqueGroups == set(self.groupsIds):
            # logger.debug("Listed groups not the same as in the week")
            self.groupsIds = list(uniqueGroups)

    def verify_dependencies(
            self,
            groupsCollection: Collection,
    ) -> bool:
        for groupId in self.groupsIds:
            if not groupsCollection.find_one({"_id": ObjectId(groupId)}):
                return False
        return True

class CallScheduleBase(BaseModel):
    name: str = Field(max_length=25)
    lessonDuration: int = Field(gt=0, lt=150)
    lessonStartTimes: list[datetime.datetime]

class UserRole(str, Enum):
    admin = "admin"
    teacher = "teacher"

class UserBase(BaseModel):
    displayName: str
    username: str = Field(min_length=1, max_length=18)
    role: UserRole
    connectedTeacher: Optional[PyObjectId]

    @field_validator("connectedTeacher")
    def connectedTeacherMustbeSetted(cls, value, values: dict):
        if value == UserRole.teacher and not values["connectedTeacher"]:
            raise ValidationError

class CredentialBase(BaseModel):
    username: str
    passwordHashed: str