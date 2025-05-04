from pymongo.collection import Collection
from fastapi import APIRouter, Depends
from FullModels import TeacherFull
from BaseModels import TeacherBase
from authx import AuthX
from utiles.WorkObjectsCRUDRoutesCreate import WorkObjectsCRUDRoutesCreate

def main(
        teachersCollection: Collection,
        security: AuthX
) -> APIRouter:
    router = APIRouter(
        prefix="/teachers",
        tags=["Teachers"]
    )

    WorkObjectsCRUDRoutesCreate(
        router=router,
        fullModel=TeacherFull,
        baseModel=TeacherBase,
        mongoCollection=teachersCollection,
        dependencies=[Depends(security.access_token_required)]
    ).SetupMethods()
    return router