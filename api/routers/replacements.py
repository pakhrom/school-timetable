import datetime
from typing import Optional

from fastapi import APIRouter
from FullModels import ReplacementsFull
from BaseModels import ReplacementsBase
from schemas.DBLoad import getListDicts
from utiles.CRUDMethods import CRUDMethods
from pymongo.collection import Collection

def main(replacementsDocsCollection: Collection) -> APIRouter:

    router = APIRouter(
        prefix="/replacements",
        tags=["Replacements"]
    )

    CRUDMethods(
        router=router,
        fullModel=ReplacementsFull,
        baseModel=ReplacementsBase,
        mongoCollection=replacementsDocsCollection
    ).SetupMethods()

    @router.get(
        path="",
        response_model=list[ReplacementsFull]
    )
    async def getReplacements(
        week: Optional[int] = None
    ):
        if week:
            today = datetime.date.today() - datetime.timedelta(7*week)
            weekStart = today - datetime.timedelta(today.weekday())
            weekEnd = weekStart + datetime.timedelta(6)
            return getListDicts(
                collection=replacementsDocsCollection,
                model=ReplacementsFull,
                filter={
                    "date": {"$lt": weekEnd, "$gte": weekStart}
                }
            )
        else:
            return getListDicts(
                collection=replacementsDocsCollection,
                model=ReplacementsFull,
            )
    return router