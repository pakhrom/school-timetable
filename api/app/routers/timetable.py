from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from pymongo.collection import Collection

from app.FullModels import TimetableFull
from app.BaseModels import TimetableBase
from app.schemas.DBLoad import getListDicts
from typing import Union, Optional, Annotated
from authx import AuthX, RequestToken, TokenPayload
from bson.objectid import ObjectId

class ListResponseModel(BaseModel):
    data: list[TimetableFull]


class headerTimetableObjectDict(BaseModel):
    className: str
    objId: str


def main(
        timetablesCollection: Collection,
        security: AuthX
) -> APIRouter:

    # authorization rules setting up
    def authVerification(
            JWTData: Annotated[TokenPayload, Depends(security.access_token_required)],
    ) -> bool:
        try:
            if JWTData.role == "admin":
                return True
            raise HTTPException(status_code=403, detail="Only admins can edit timetable")
        except Exception as e:
            raise HTTPException(status_code=401, detail={"message": str(e)})

    router = APIRouter(
        prefix="/timetables",
        tags=["Timetables"]
    )

    @router.get(
        path="/{objId}",
        response_model=TimetableFull,
        description="Get one object Subject by objId"
    )
    async def GetOne(objId: str):
        try:
            response = getListDicts(
                collection=timetablesCollection,
                model=TimetableFull,
                filter={"_id": ObjectId(objId)})
            return response[0]
        except IndexError:
            raise IndexError(f"Obj with Id: {objId} can`t be found")

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @router.get(
        path="",
        response_model=Union[ListResponseModel, list[headerTimetableObjectDict]],
        description="Get list of full objects Subject"
    )
    async def all(isSimplifiedReturn: Optional[bool] = None):
        if not isSimplifiedReturn:
            return ListResponseModel(
                data=getListDicts(
                    collection=timetablesCollection,
                    model=TimetableFull,
                )
            )
        return getListDicts(
            collection=timetablesCollection,
            model=headerTimetableObjectDict,
            projection={"className"}
        )

    @router.delete(
        path="/{objId}",
        dependencies=[Depends(authVerification)]
    )
    async def DeleteOne(objId: str, token: Annotated[RequestToken, Depends(security.access_token_required)] ):
        authVerification(
            security=security,
            token=token
        )
        try:
            timetablesCollection.delete_one({"_id": ObjectId(objId)})
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @router.put(
        path="/{objId}",
        dependencies=[Depends(authVerification)]
    )
    async def UpdateOne(objId: str, timetable: TimetableFull):
        try:
            timetablesCollection.update_one({"_id": ObjectId(objId)}, {"$set": TimetableFull(
                **timetable.model_dump()
            ).model_dump(exclude={"objId"})})
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @router.post(
        path="",
        dependencies=[Depends(authVerification)]
    )
    async def CreateOne(timetable: TimetableBase):
        try:
            result = timetablesCollection.insert_one(
                TimetableFull(**timetable.model_dump()).model_dump(exclude={"objId"})
            )
            return str(result.inserted_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return router
