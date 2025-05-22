import datetime
import logging
from typing import Optional, Annotated
from pydantic import BaseModel, field_validator, ValidationError, Field, model_validator
from enum import Enum
# import hashlib
from pymongo.synchronous.collection import Collection
from bson import ObjectId


class SubjectBase(BaseModel):
    shortName: str = Field(min_length=1, max_length=10)
    fullName: str = Field(min_length=1, max_length=20)
    optional: bool = False
    groupsIds: list[str] = []

class GroupBase(BaseModel):
    subjectId: str = Field(min_length=24, max_length=24)
    teacherId: str = Field(min_length=24, max_length=24)
    cabinet: str = Field(min_length=3, max_length=20)
    attendPeriodicity: int = Field(gt=0)

    @classmethod
    def pairGroup(
            cls,
            collection: Collection | list[Collection],
            addId: str,
            selectId: str | list[str],
    ):
        def pairOneElement(
                collection: Collection,
                addId: str,
                selectId: str,
        ):
            pairedGroups: list[str] = collection.find_one(
                filter={"_id": ObjectId(selectId)}
            )["groupsIds"]

            pairedGroups.append(addId)

            return collection.update_one(
                filter={"_id": ObjectId(selectId)},
                update={"$set": {
                    "groupsIds": pairedGroups,
                    "updateDate": datetime.datetime.now()
                }}
            )

        if type(selectId) == list and type(collection) == list:
            for oneSelectId, oneCollection in zip(selectId, collection):
                pairOneElement(
                    collection=oneCollection,
                    addId=addId,
                    selectId=oneSelectId
                )

        elif type(selectId) == str and type(collection) == Collection:
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
            delId: str,
            selectId: str | list[str],
    ):
        def unpairOneElement(
                collection: Collection,
                delId: str,
                selectId: str,
        ):
            pairedGroups: list[str] = collection.find_one(
                filter={"_id": ObjectId(selectId)}
            )["groupsIds"]

            pairedGroups.remove(delId)

            return collection.update_one(
                filter={"_id": ObjectId(selectId)},
                update={"$set": {
                    "groupsIds": pairedGroups,
                    "updateDate": datetime.datetime.now()
                }}
            )

        if type(selectId) == list and type(collection) == list:
            for oneSelectId, oneCollection in zip(selectId, collection):
                unpairOneElement(
                    collection=oneCollection,
                    delId=delId,
                    selectId=oneSelectId
                )

        elif type(selectId) == str and type(collection) == Collection:
            unpairOneElement(
                collection=collection,
                delId=delId,
                selectId=selectId
            )
        else:
            raise TypeError("Pass all lists of elements or single element")

        return 0

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
    groupsIds: list[Annotated[str, Field(min_length=24, max_length=24)]] = []

class Replacement(BaseModel):
    lesson: int = Field(gt=0, lt=13)
    reason: Optional[str] = Field(max_length=20)
    oldGroupId: str = Field(min_length=24, max_length=24)
    newGroupId: Optional[str] = Field(min_length=24, max_length=24)

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
    callScheduleId: Optional[str] = Field(min_length=24, max_length=24)

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
    groupsIds: list[Annotated[str, Field(min_length=24, max_length=24)]] = []
    weekIds: list[Annotated[
        list[Annotated[list[
            Annotated[str, Field(min_length=24, max_length=24)]  # groupId
        ], Field(min_length=0, max_length=13)]
        ], Field(min_length=6, max_length=7)
    ]]

    @model_validator(mode="after")
    def groups_is_equal(
            self
    ):
        # logger = logging.getLogger("uvicorn.debug")
        uniqueGroups = set()
        for day in self.weekIds:
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
    username: str = Field(max_length=18)
    role: UserRole
    connectedTeacher: Optional[str] = Field(min_length=24, max_length=24)

    @field_validator("connectedTeacher")
    def connectedTeacherMustbeSetted(cls, value, values: dict):
        if value == UserRole.teacher and not values["connectedTeacher"]:
            raise ValidationError

class CredentialBase(BaseModel):
    username: str
    passwordHashed: str