from pymongo.collection import Collection
from fastapi import APIRouter, Depends, HTTPException
from app.BaseModels import SubjectBase
from app.FullModels import SubjectFull
from authx import AuthX, TokenPayload
from app.schemas.DBLoad import getListDicts
from bson.objectid import ObjectId
from typing import Annotated

def main(
        subjectCollection: Collection,
        security: AuthX
) -> APIRouter:

    def authorization(
            JWTData: Annotated[TokenPayload, Depends(security.access_token_required)]
    ):
        if JWTData.role != "admin":
            raise HTTPException(
                status_code=403,
                detail="Only admins can edit teachers"
            )
        return True

    router = APIRouter(
        prefix="/subjects",
        tags=["Subject"]
    )

    @router.get(
        path="",
        response_model=list[SubjectFull],
    )
    async def GetAll():
        return getListDicts(
            collection=subjectCollection,
            model=SubjectFull
        )

    @router.get(
        path="/{objId}",
        response_model=SubjectFull,
    )
    async def GetOne(objId: str):
        return getListDicts(
            collection=subjectCollection,
            model=SubjectFull,
            query={"_id": ObjectId(objId)}
        )[0]

    @router.post(
        path="",
        response_model=str,
        dependencies=[Depends(authorization)]
    )
    async def CreateOne(subject: SubjectBase):
        result = subjectCollection.insert_one(
            SubjectFull(**subject.model_dump()).model_dump(exclude={"objId"})
        )
        return str(result.inserted_id)

    @router.put(
        path="/{objId}",
        dependencies=[Depends(authorization)]
    )
    async def UpdateOne(objId: str, subject: SubjectBase):
        subjectCollection.update_one(
            {"_id": ObjectId(objId)},
            {"$set": SubjectFull(**subject.model_dump()).model_dump(exclude={"objId"})}
        )

    @router.delete(
        path="/{objId}",
        response_model=int,
        dependencies=[Depends(authorization)]
    )
    async def DeleteOne(objId: str):
        subjectCollection.delete_one({"_id": ObjectId(objId)})

    return router
