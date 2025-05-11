from fastapi import APIRouter, Depends, HTTPException
from app.BaseModels import CallScheduleBase
from app.FullModels import CallScheduleFull
from pymongo.collection import Collection
from authx import AuthX, TokenPayload
from typing import Annotated
from app.utiles.dataPreprocessing import processForDB
from app.schemas.DBLoad import getListDicts
from bson import ObjectId

def main(
        callScheduleCollection: Collection,
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
        prefix="/call-schedules",
        tags=["Call Schedule"]
    )

    @router.get(
        path="",
        response_model=list[CallScheduleFull]
    )
    async def GetAll():
        return getListDicts(
            collection=callScheduleCollection,
            model=CallScheduleFull
        )

    @router.get(
        path="/{onjId}",
        response_model=CallScheduleFull
    )
    async def GetOne(objId: str):
        try:
            return getListDicts(
                collection=callScheduleCollection,
                model=CallScheduleFull,
                filter={"_id": ObjectId(objId)}
            )[0]
        except IndexError as e:
            raise HTTPException(status_code=404, detail="CallSchedule not found")

    @router.post(
        path="",
        dependencies=[Depends(authorization)],
        response_model=str
    )
    async def CreateOne(group: CallScheduleBase):
        response = callScheduleCollection.insert_one(processForDB(
            baseObject=group,
            fullModel=CallScheduleFull
        ))
        return ObjectId(response.inserted_id)

    @router.put(
        path="/{objId}",
        dependencies=[Depends(authorization)]
    )
    async def UpdateOne(objId: str, group: CallScheduleBase):
        response = callScheduleCollection.update_one(
            {"_id": ObjectId(objId)},
            {"$set": processForDB(group, CallScheduleFull)}
        )
        if response.modified_count == 0:
            raise HTTPException(status_code=404, detail="CallSchedule not found")

    @router.delete(
        path="/{objId}",
        dependencies=[Depends(authorization)]
    )
    async def DeleteOne(objId: str):
        response = callScheduleCollection.delete_one({"_id": ObjectId(objId)})

        if response.deleted_count == 0:
            raise HTTPException(status_code=404, detail="CallSchedule not found")

    return router