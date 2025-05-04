import datetime
from typing import Optional

from fastapi import APIRouter, Depends
from FullModels import ReplacementsFull
from BaseModels import ReplacementsBase
from schemas.DBLoad import getListDicts
from utiles.WorkObjectsCRUDRoutesCreate import WorkObjectsCRUDRoutesCreate
from pymongo.collection import Collection
from authx import AuthX

def main(
        replacementsDocsCollection: Collection,
        security: AuthX
) -> APIRouter:

    router = APIRouter(
        prefix="/replacements",
        tags=["Replacements"]
    )

    WorkObjectsCRUDRoutesCreate(
        router=router,
        fullModel=ReplacementsFull,
        baseModel=ReplacementsBase,
        mongoCollection=replacementsDocsCollection,
        dependencies=[Depends(security.access_token_required)]
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