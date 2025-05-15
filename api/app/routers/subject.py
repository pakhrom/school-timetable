from pymongo.collection import Collection
from fastapi import APIRouter, Depends, HTTPException, Header
from app.BaseModels import SubjectBase
from app.FullModels import SubjectFull
from authx import AuthX, TokenPayload, RequestToken
from app.schemas.DBLoad import getListDicts
from bson.objectid import ObjectId
from typing import Annotated

def main(
        subjectCollection: Collection,
        security: AuthX
) -> APIRouter:

    def authorization(
            token: str = Header(),
    ) -> bool:
        JWTData = security.verify_token(RequestToken(
            token=token,
            location="headers"
        ))
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
        path="/{id}",
        response_model=SubjectFull,
    )
    async def GetOne(id: str):
        return getListDicts(
            collection=subjectCollection,
            model=SubjectFull,
            filter={"_id": ObjectId(id)}
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
        path="/{id}",
        dependencies=[Depends(authorization)]
    )
    async def UpdateOne(id: str, subject: SubjectBase):
        subjectCollection.update_one(
            {"_id": ObjectId(id)},
            {"$set": SubjectFull(**subject.model_dump()).model_dump(exclude={"objId"})}
        )

    @router.delete(
        path="/{id}",
        dependencies=[Depends(authorization)]
    )
    async def DeleteOne(id: str):
        subject: SubjectFull = getListDicts(
            collection=subjectCollection,
            model=SubjectFull,
            filter={"_id": ObjectId(id)}
        )[0]
        if subject.groupsIds != []:
            raise HTTPException(409, "Subject still connected to other objects")
        subjectCollection.delete_one({"_id": ObjectId(id)})

    return router
