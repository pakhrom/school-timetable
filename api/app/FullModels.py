# import datetime
# from typing import Optional
from pydantic import BaseModel
# from enum import Enum
import app.BaseModels as bm
import datetime
from typing import Optional

class _AllServerBase(BaseModel):
    objId: Optional[str] = None
    updateDate: datetime.datetime = datetime.datetime.now()

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