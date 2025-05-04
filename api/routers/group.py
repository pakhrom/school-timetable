from fastapi import APIRouter, Depends
from BaseModels import GroupBase
from FullModels import GroupFull
from utiles.WorkObjectsCRUDRoutesCreate import WorkObjectsCRUDRoutesCreate
from pymongo.collection import Collection
from authx import AuthX

def main(
        groupsCollection: Collection,
        security: AuthX
) -> APIRouter:

    router = APIRouter(
        prefix="/groups",
        tags=["Group"]
    )

    WorkObjectsCRUDRoutesCreate(
        router=router,
        fullModel=GroupFull,
        baseModel=GroupBase,
        mongoCollection=groupsCollection,
        dependencies=[Depends(security.access_token_required)]
    ).SetupMethods()
    return router