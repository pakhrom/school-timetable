from fastapi import APIRouter, Depends, HTTPException, Header
from app.BaseModels import GroupBase
from app.FullModels import GroupFull

from pymongo.collection import Collection
from authx import AuthX, TokenPayload, RequestToken
from typing import Annotated
from app.schemas.DBLoad import getListDicts
from bson.objectid import ObjectId
from app.utiles.dataPreprocessing import processForDB

def main(
        groupsCollection: Collection,
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
        prefix="/groups",
        tags=["Group"]
    )

    @router.get(
        path="",
        response_model=list[GroupFull]
    )
    async def GetAll():
        return getListDicts(
            collection=groupsCollection,
            model=GroupFull
        )

    @router.get(
        path="/{objId}",
        response_model=GroupFull
    )
    async def GetOne(objId: str):
        try:
            return getListDicts(
                collection = groupsCollection,
                model = GroupFull,
                filter = {"_id": ObjectId(objId)}
            )[0]
        except IndexError as e:
            raise HTTPException(status_code=404, detail="Group not found")

    @router.post(
        path="",
        dependencies=[Depends(authorization)],
        response_model=str
    )
    async def CreateOne(group: GroupBase):
        response = groupsCollection.insert_one(processForDB(
            baseObject=group,
            fullModel=GroupFull
        ))
        return ObjectId(response.inserted_id)

    @router.put(
        path="/{objId}",
        dependencies=[Depends(authorization)]
    )
    async def UpdateOne(objId: str, group: GroupBase):
        response = groupsCollection.update_one(
            {"_id": ObjectId(objId)},
            {"$set": processForDB(group, GroupFull)}
        )
        if response.modified_count == 0:
            raise HTTPException(status_code=404, detail="Group not found")

    @router.delete(
        path="/{objId}",
        dependencies=[Depends(authorization)]
    )
    async def DeleteOne(objId: str):
        response = groupsCollection.delete_one({"_id": ObjectId(objId)})

        if response.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Group not found")

    return router