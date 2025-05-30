import logging

from fastapi import APIRouter, Depends, HTTPException, Header
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
        groupsCollection: Collection,
        security: AuthX,
) -> APIRouter:

    # authorization rules setting up
    def authVerification(
            token: str = Header(),
    ) -> bool:
        JWTData = security.verify_token(RequestToken(
            token=token,
            location="headers"
        ))
        if JWTData.role == "admin":
            return True
        raise HTTPException(status_code=403, detail="Only admins can edit timetable")

    router = APIRouter(
        prefix="/timetables",
        tags=["Timetables"]
    )

    @router.get(
        path="/{objId}",
        description="Get one object Subject by objId"
    )
    async def GetOne(objId: str):
        try:
            response:TimetableFull = getListDicts(
                collection=timetablesCollection,
                model=TimetableFull,
                filter={"_id": ObjectId(objId)})[0]
            return response.printOut(groupsCollection=groupsCollection)
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
    async def DeleteOne(objId: str):
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
            if not timetable.verify_dependencies(
                groupsCollection=groupsCollection
            ):
                raise HTTPException(422, "Cant verify timetable")
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
            if timetable.week:
                if not timetable.verify_dependencies(
                    groupsCollection=groupsCollection
                ):
                    raise HTTPException(422, "Cant verify timetable")
            result = timetablesCollection.insert_one(
                TimetableFull(**timetable.model_dump()).model_dump(exclude={"objId"})
            )
            return str(result.inserted_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return router