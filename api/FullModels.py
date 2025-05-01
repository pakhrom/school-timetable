# import datetime
# from typing import Optional
from pydantic import BaseModel
# from enum import Enum
import BaseModels as rdt
import datetime
from typing import Optional

class _AllServerBase(BaseModel):
    objId: Optional[str] = None
    updateDate: datetime.datetime = datetime.datetime.now()

class TimetableFull(rdt.TimetableBase, _AllServerBase):
    pass

class TeacherFull(rdt.TeacherBase, _AllServerBase):
    pass

class SubjectFull(rdt.SubjectBase, _AllServerBase):
    pass

class ReplacementsFull(rdt.ReplacementsBase, _AllServerBase):
    pass

class GroupFull(rdt.GroupBase, _AllServerBase):
    pass

class CallScheduleFull(rdt.CallScheduleBase, _AllServerBase):
    pass