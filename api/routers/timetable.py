from fastapi import APIRouter
from pydantic import BaseModel
from pymongo.collection import Collection
import logging

from FullModels import TimetableFull
from BaseModels import TimetableBase
from utiles.CRUDMethods import CRUDMethods
from schemas.DBLoad import getListDicts
from typing import Union, Optional

def main(timetablesCollection: Collection) -> APIRouter:

    router = APIRouter(
        prefix="/timetables",
        tags=["Timetables"]
    )

    methods = CRUDMethods(
        router=router,
        fullModel=TimetableFull,
        baseModel=TimetableBase,
        mongoCollection=timetablesCollection
    )
    methods.AddOne()
    methods.UpdateOne()
    methods.GetOne()
    methods.DeleteOne()

    class ListResponseModel(BaseModel):
        data: list[TimetableFull]

    class headerTimetableObjectDict(BaseModel):
        className: str
        objId: str

    @router.get(
        path="",
        response_model=Union[ListResponseModel, list[headerTimetableObjectDict]],
        description="Get list of full objects Subject"
    )
    async def all(isSimplifiedReturn: Optional[bool] = None):
        if not isSimplifiedReturn:
            return ListResponseModel(
                data=getListDicts(
                    collection=timetablesCollection,
                    model=TimetableFull,
                )
            )
        return getListDicts(
            collection=timetablesCollection,
            model=headerTimetableObjectDict,
            projection={"className"}
        )



    return router