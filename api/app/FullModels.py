# import datetime
# from typing import Optional
import logging

from pydantic import BaseModel, BeforeValidator, Field, AliasChoices, ValidationError
# from enum import Enum
import app.BaseModels as bm
import datetime
from typing import Optional, Annotated
from bson import ObjectId
from pymongo.synchronous.collection import Collection


PyObjectId = Annotated[str, BeforeValidator(str)]

class _AllServerBase(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    objId: Optional[PyObjectId] | Optional[str] = Field(
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


class TimetableFull(bm.TimetableBase, _AllServerBase):
    pass

class TeacherFull(bm.TeacherBase, _AllServerBase):
    pass

class SubjectFull(bm.SubjectBase, _AllServerBase):
    pass

class ReplacementsFull(bm.ReplacementsBase, _AllServerBase):
    pass

class GroupFull(bm.GroupBase, _AllServerBase):
    pass

class CallScheduleFull(bm.CallScheduleBase, _AllServerBase):
    pass

class UserFull(bm.UserBase, _AllServerBase):
    pass

class CredentialFull(bm.CredentialBase, _AllServerBase):
    pass