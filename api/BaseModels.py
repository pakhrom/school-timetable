import datetime
from typing import Optional
from pydantic import BaseModel
from enum import Enum


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
    oldGroupId: int
    newGroupId: Optional[int]

class ReplacementsBase(BaseModel):
    date: datetime.datetime
    modifiedGroups: Optional[list[Replacement]] = []

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