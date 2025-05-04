from pymongo.collection import Collection
from fastapi import APIRouter, Depends
from BaseModels import SubjectBase
from FullModels import SubjectFull
from authx import AuthX
from utiles.WorkObjectsCRUDRoutesCreate import WorkObjectsCRUDRoutesCreate

def main(
        subjectCollection: Collection,
        security: AuthX
) -> APIRouter:

    router = APIRouter(
        prefix="/subjects",
        tags=["Subject"]
    )

    WorkObjectsCRUDRoutesCreate(
        fullModel=SubjectFull,
        baseModel=SubjectBase,
        router=router,
        mongoCollection=subjectCollection,
        dependencies=[Depends(security.access_token_required)]
    ).SetupMethods()
    return router