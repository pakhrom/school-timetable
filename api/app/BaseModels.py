import datetime
from typing import Optional
from pydantic import BaseModel, field_validator, ValidationError
from enum import Enum
import hashlib


class SubjectBase(BaseModel):
    shortName: str
    fullName: str
    isNeedToAttend: bool

class GroupBase(BaseModel):
    subjectId: int
    teacherId: int
    cabinet: str
    attendPeriodicity: int

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
    groupsIds: list[int]
    week: list[
        list[
            list[
                int # groupId
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