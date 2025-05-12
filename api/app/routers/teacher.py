from pymongo.collection import Collection
from fastapi import APIRouter, Depends, HTTPException, Header
from app.FullModels import TeacherFull
from app.BaseModels import TeacherBase
from app.schemas.DBLoad import getListDicts
from authx import AuthX, TokenPayload, RequestToken
from bson.objectid import ObjectId
from typing import Annotated

def main(
        teachersCollection: Collection,
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
        prefix="/teachers",
        tags=["Teachers"]
    )

    @router.get(
        path="",
        response_model=list[TeacherFull]
    )
    async def GetAll():
        teachersCollection.find()
        return getListDicts(
            teachersCollection,
            TeacherFull
        )

    @router.get(
        path="/{id}",
        response_model=TeacherFull
    )
    async def GetOne(id: str):
        return getListDicts(
            collection=teachersCollection,
            model=TeacherFull,
            filter={"_id": ObjectId(id)}
        )[0]

    @router.post(
        path="",
        response_model=str,
        dependencies=[Depends(authorization)]
    )
    async def CreateOne(data: TeacherBase):
        return str(teachersCollection.insert_one(
            TeacherFull(**data.model_dump()).model_dump(exclude={"objId"})
        ).inserted_id)

    @router.put(
        path="/{id}",
        dependencies=[Depends(authorization)]
    )
    async def UpdateOne(id: str, data: TeacherBase):
        result = teachersCollection.update_one({"_id": ObjectId(id)}, {"$set": TeacherFull(
            **data.model_dump()
        ).model_dump(exclude={"objId"})})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Teacher not found")

    @router.delete(
        path="/{id}",
        dependencies=[Depends(authorization)]
    )
    async def DeleteOne(id: str):
        result = teachersCollection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Teacher not found")

    return router
