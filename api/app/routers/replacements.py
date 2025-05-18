import datetime
from sys import prefix
from typing import Optional, Annotated

from fastapi import APIRouter, Depends, HTTPException, Header
from app.FullModels import ReplacementsFull
from app.BaseModels import ReplacementsBase
from app.schemas.DBLoad import getListDicts
from pymongo.collection import Collection
from authx import AuthX, TokenPayload, RequestToken
from bson.objectid import ObjectId
from app.utiles.dataPreprocessing import processForDB
from .replacement import replacement

def main(
        replacementsDocsCollection: Collection,
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
        prefix="/replacements",
        tags=["Replacements"]
    )

    @router.get(
        path="",
        response_model=list[ReplacementsFull]
    )
    async def getReplacements(
        week: Optional[int] = None
    ):
        if week:
            today = datetime.date.today() - datetime.timedelta(7*week)
            weekStart = today - datetime.timedelta(today.weekday())
            weekEnd = weekStart + datetime.timedelta(6)
            return getListDicts(
                collection=replacementsDocsCollection,
                model=ReplacementsFull,
                filter={
                    "date": {"$lt": weekEnd, "$gte": weekStart}
                }
            )
        else:
            return getListDicts(
                collection=replacementsDocsCollection,
                model=ReplacementsFull,
            )

    @router.get(
        path="/{objId}",
        response_model=ReplacementsFull
    )
    async def GetOne(objId: str):
        try:
            response = getListDicts(
                collection=replacementsDocsCollection,
                model=ReplacementsFull,
                filter={"objId": objId}
            )
            return response[0]
        except IndexError:
            raise HTTPException(status_code=404, detail="Object not found")

    @router.post(
        path="",
        response_model=str,
        dependencies=[Depends(authorization)]
    )
    async def CreateOne(replacement: ReplacementsBase):
        response = replacementsDocsCollection.insert_one(
            ReplacementsFull(**replacement.model_dump()).model_dump(exclude={"objId"})
        )
        return str(response.inserted_id)

    @router.put(
        path="/{objId}",
        dependencies=[Depends(authorization)],
    )
    async def UpdateOne(objId: str, replacements: ReplacementsBase):
        response = replacementsDocsCollection.update_one(
            {"_id": ObjectId(objId)},
            {"$set": processForDB(replacements, ReplacementsFull)}
        )

        return {
            "details": f"Updated {response.modified_count} objects"
        }


    @router.delete(
        path="/{objId}",
        dependencies=[Depends(authorization)],
    )
    async def DeleteOne(objId: str):
        replacementsDocsCollection.delete_one({"_id": ObjectId(objId)})
        return {
            "details": "deleting success"
        }

    # Entry point for single replacement

    router.include_router(
        replacement.main(
            security, replacementsDocsCollection, groupsCollection
        ),
        prefix="/{replacementsObjId}"
    )

    return router
