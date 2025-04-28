from fastapi import APIRouter
from BaseModels import GroupBase
from FullModels import GroupFull
from utiles.CRUDMethods import CRUDMethods
from pymongo.collection import Collection

def main(groupsCollection: Collection) -> APIRouter:

    router = APIRouter(
        prefix="/groups",
        tags=["Group"]
    )

    CRUDMethods(
        router=router,
        fullModel=GroupFull,
        baseModel=GroupBase,
        mongoCollection=groupsCollection,
    ).SetupMethods()
    return router