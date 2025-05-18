import datetime
from typing import Optional
from pydantic import BaseModel, field_validator, ValidationError, Field
from enum import Enum
import hashlib
from pymongo.synchronous.collection import Collection
from bson import ObjectId


class SubjectBase(BaseModel):
    shortName: str
    fullName: str
    optional: bool
    groupsIds: list[str] = []

class GroupBase(BaseModel):
    subjectId: str
    teacherId: str
    cabinet: str
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

    def printOut(
            self,
            subjectsCollection: Collection,
            teacherCollection: Collection,
    ):
        from FullModels import SubjectFull, TeacherFull
        return self.model_dump(
            exclude={"subjectId", "teacherId"}
        ) | {
            "subject": SubjectFull(**subjectsCollection.find_one({"_id": ObjectId(self.subjectId)})),
            "teacher": TeacherFull(**teacherCollection.find_one({"_id": ObjectId(self.teacherId)}))
        }

    def verify_dependencies(
            self,
            teachersCollection: Collection,
            subjectsCollection: Collection,
    ) -> bool:
        from FullModels import TeacherFull, SubjectFull
        teacherVer = TeacherFull(
            **teachersCollection.find_one({"_id": ObjectId(self.teacherId)})
        ).verify(teachersCollection)
        subjectVer = SubjectFull(
            **subjectsCollection.find_one({"_id": ObjectId(self.subjectId)})
        ).verify(subjectsCollection)
        return teacherVer * subjectVer

class Gender(str, Enum):
    male = 'male'
    female = 'female'

class FullName(BaseModel):
    first: str
    last: str
    middle: str

class TeacherBase(BaseModel):
    gender: Gender
    fullname: FullName
    groupsIds: list[str] = []

class Replacement(BaseModel):
    lesson: int
    reason: Optional[str]
    oldGroupId: str
    newGroupId: Optional[str]

class ReplacementsBase(BaseModel):
    date: datetime.datetime
    modifiedGroups: Optional[list[Replacement]] = []
    callScheduleId: Optional[str]

class TimetableBase(BaseModel):
    className: str
    groupsIds: list[str]
    week: list[
        list[
            list[
                str # groupId
            ]
        ]
    ]

class CallScheduleBase(BaseModel):
    name: str
    lessonDuration: int
    lessonStartTimes: list[datetime.datetime]

class UserRole(str, Enum):
    admin = "admin"
    teacher = "teacher"

class UserBase(BaseModel):
    displayName: str
    username: str
    role: UserRole
    connectedTeacher: Optional[str]

    @field_validator("connectedTeacher")
    def connectedTeacherMustbeSetted(cls, value, values: dict):
        if value == UserRole.teacher and not values["connectedTeacher"]:
            raise ValidationError

class CredentialBase(BaseModel):
    username: str
    passwordHashed: str