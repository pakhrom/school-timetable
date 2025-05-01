from fastapi import APIRouter
from BaseModels import CallScheduleBase
from FullModels import CallScheduleFull
from utiles.CRUDMethods import CRUDMethods
from pymongo.collection import Collection

def main(callScheduleCollection: Collection) -> APIRouter:

    router = APIRouter(
        prefix="/call-schedule",
        tags=["Call Schedule"]
    )

    CRUDMethods(
        router=router,
        fullModel=CallScheduleFull,
        baseModel=CallScheduleBase,
        mongoCollection=callScheduleCollection
    ).SetupMethods()
    return router