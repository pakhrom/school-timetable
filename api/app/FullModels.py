# import datetime
# from typing import Optional
import logging

import bson.errors
from pydantic import BaseModel, Field, AliasChoices, ValidationError
# from enum import Enum
import app.BaseModels as bm
import datetime
from typing import Optional, Annotated
from bson import ObjectId
from pymongo.synchronous.collection import Collection



class _AllServerBase(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    objId: Optional[bm.PyObjectId] = Field(
        default=None,
        validation_alias=AliasChoices('objId', '_id'),
        serialization_alias='objId'
    )
    updateDate: datetime.datetime = datetime.datetime.now()

    def verify(
            self,
            objCollection: Collection,
    ) -> bool:

        logger = logging.getLogger("uvicorn.debug")
        DBResponse = objCollection.find_one({"_id": ObjectId(self.objId)})

        if not DBResponse:
            logger.debug(f"No object {self.__name__} - verification failed")
            return False

        tempModel = self.model_copy()
        try:
            tempModel.model_validate(**DBResponse)
        except ValidationError as e:
            logger.debug(f"Failed to validate {self.__name__}:\n{e}")
            return False

        return True


class TeacherFull(bm.TeacherBase, _AllServerBase):
    pass

class SubjectFull(bm.SubjectBase, _AllServerBase):
    pass

class ReplacementsFull(bm.ReplacementsBase, _AllServerBase):
    pass

class GroupPrintOut(_AllServerBase):
    subject: SubjectFull
    teacher: TeacherFull
    cabinet: str = Field(min_length=3, max_length=20)

class GroupFull(bm.GroupBase, _AllServerBase):
    def printOut(
            self,
            subjectsCollection: Collection,
            teacherCollection: Collection,
    ):
        return self.model_dump(
            exclude={"subjectId", "teacherId"}
        ) | {
            "subject": SubjectFull(**subjectsCollection.find_one({"_id": ObjectId(self.subjectId)})),
            "teacher": TeacherFull(**teacherCollection.find_one({"_id": ObjectId(self.teacherId)}))
        }

class CallScheduleFull(bm.CallScheduleBase, _AllServerBase):
    pass

class UserFull(bm.UserBase, _AllServerBase):
    pass

class CredentialFull(bm.CredentialBase, _AllServerBase):
    pass

class TimetablePrintOut(_AllServerBase):
    className: str = Field(min_length=2, max_length=10)
    week: Annotated[
        list[
            Annotated[
                list[Optional[list[GroupFull]]],  # Список уроков (0-13 элементов)
                Field(min_length=0, max_length=13)
            ]
        ],
        Field(min_length=5, max_length=7)  # Неделя (5-7 дней)
    ]

class TimetableFull(bm.TimetableBase, _AllServerBase):
    def printOut(
            self,
            groupsCollection: Collection,
    ) -> TimetablePrintOut:
        logger = logging.getLogger("uvicorn.debug")
        logger.info(self.week[0][0][0])
        week = [
            [
                [
                    GroupFull(**groupsCollection.find_one({"_id": ObjectId(groupId)})) if groupId else None
                    for groupId in lesson
                ] if lesson else lesson
                for lesson in day
            ]
            for day in self.week
        ]
        return TimetablePrintOut(
            objId = self.objId,
            updateDate = self.updateDate,
            className = self.className,
            week = week
        )