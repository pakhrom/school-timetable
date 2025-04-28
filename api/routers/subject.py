from pymongo.collection import Collection
from fastapi import APIRouter
from BaseModels import SubjectBase
from FullModels import SubjectFull
from utiles.CRUDMethods import CRUDMethods

def main(subjectCollection: Collection) -> APIRouter:

    router = APIRouter(
        prefix="/subjects",
        tags=["Subject"]
    )

    CRUDMethods(
        fullModel=SubjectFull,
        baseModel=SubjectBase,
        router=router,
        mongoCollection=subjectCollection
    ).SetupMethods()
    return router