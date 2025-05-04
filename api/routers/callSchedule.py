from fastapi import APIRouter, Depends
from BaseModels import CallScheduleBase
from FullModels import CallScheduleFull
from utiles.WorkObjectsCRUDRoutesCreate import WorkObjectsCRUDRoutesCreate
from pymongo.collection import Collection
from authx import AuthX

def main(
        callScheduleCollection: Collection,
        security: AuthX
) -> APIRouter:

    router = APIRouter(
        prefix="/call-schedules",
        tags=["Call Schedule"]
    )

    WorkObjectsCRUDRoutesCreate(
        router=router,
        fullModel=CallScheduleFull,
        baseModel=CallScheduleBase,
        mongoCollection=callScheduleCollection,
        dependencies=[Depends(security.access_token_required)]
    ).SetupMethods()
    return router