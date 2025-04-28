from pymongo.collection import Collection
from fastapi import APIRouter
from FullModels import TeacherFull
from BaseModels import TeacherBase
from utiles.CRUDMethods import CRUDMethods

def main(teachersCollection: Collection) -> APIRouter:
    router = APIRouter(
        prefix="/teachers",
        tags=["Teachers"]
    )

    CRUDMethods(
        router=router,
        fullModel=TeacherFull,
        baseModel=TeacherBase,
        mongoCollection=teachersCollection
    ).SetupMethods()
    return router