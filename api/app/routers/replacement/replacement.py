import datetime
from typing import Optional, Annotated

import bson.errors
from pydantic import BaseModel

from fastapi import APIRouter, Depends, HTTPException, Request
from app.FullModels import ReplacementsFull, GroupFull
from app.BaseModels import ReplacementsBase, Replacement
from app.schemas.DBLoad import getListDicts
from pymongo.collection import Collection
from authx import AuthX, TokenPayload
from bson.objectid import ObjectId
import logging

def main(
        # replacementsObjId: ObjectId,
        security: AuthX,
        replacementsDocsCollection: Collection,
        groupsCollection: Collection
) -> APIRouter:

    def authorization_post(
            replacementObj: Replacement,
            JWTData: Annotated[TokenPayload, Depends(security.access_token_required)]
    ):
        try:

            if JWTData.role == "admin":
                return True

            selectedGroup: GroupFull = getListDicts(
                collection=groupsCollection,
                model=GroupFull,
                filter={"_id": ObjectId(replacementObj.oldGroupId)}
            )[0]
            if selectedGroup.teacherId == JWTData.connectedTeacher:
                return True

            raise HTTPException(403, "You not permitted to create a replacement")

        except HTTPException as e:
            raise HTTPException(e.status_code, e.detail)
        except bson.errors.InvalidId as e:
            raise HTTPException(422, str(e))
        except Exception as e:
            raise HTTPException(500, str(e))

    def authorization_delete(
            replacementIndex: int,
            replacementsObjId: str,
            JWTData: Annotated[TokenPayload, Depends(security.access_token_required)]
    ):
        try:
            if JWTData.role == "admin":
                return True

            selectedReplacementsDoc: ReplacementsFull = getListDicts(
                collection=replacementsDocsCollection,
                model=ReplacementsFull,
                filter={"_id": ObjectId(replacementsObjId)}
            )[0]

            selectedGroup: GroupFull = getListDicts(
                collection=groupsCollection,
                model=GroupFull,
                filter={"_id": ObjectId(
                    selectedReplacementsDoc.modifiedGroups[replacementIndex].oldGroupId
                )}
            )[0]
            if selectedGroup.teacherId == JWTData.connectedTeacher:
                return True

            raise HTTPException(403, "You not permitted to create a replacement")

        except HTTPException as e:
            raise HTTPException(e.status_code, e.detail)
        except bson.errors.InvalidId as e:
            raise HTTPException(422, str(e))
        except Exception as e:
            raise HTTPException(500, str(e))


    router = APIRouter(
        prefix="/replacement",
        tags=["single-replacement"]
    )

    @router.post(
        path="",
        dependencies=[Depends(authorization_post)]
    )
    async def addReplacement(
            replacementObj: Replacement,
            replacementsObjId: str
    ):
        try:
            selectedReplacementsDoc: list[ReplacementsFull] = getListDicts(
                collection=replacementsDocsCollection,
                model=ReplacementsFull,
                filter={"_id": ObjectId(replacementsObjId)}
            )
            if len(selectedReplacementsDoc) == 0:
                raise HTTPException(404, "Replacement id must be wrong, check it")
            selectedReplacementsDoc: ReplacementsFull = selectedReplacementsDoc[0]
            selectedReplacementsDoc.modifiedGroups.append(replacementObj)
            replacementsDocsCollection.update_one(
                filter={"_id": ObjectId(replacementsObjId)},
                update={"$set": {
                    "modifiedGroups": selectedReplacementsDoc.modifiedGroups
                }}
            )

        except HTTPException as e:
            raise HTTPException(e.status_code, e.detail)
        except bson.errors.InvalidId as e:
            raise HTTPException(422, str(e))
        except Exception as e:
            raise HTTPException(500, str(e))

    @router.delete(
        path="",
        dependencies=[Depends(authorization_delete)]
    )
    async def addReplacement(
            replacementIndex: int,
            replacementsObjId: str
    ):
        """

        :param replacementIndex: index of element in Replacements object
        :param replacementsObjId:
        :return:
        """
        try:

            selectedReplacementsDoc: ReplacementsFull = getListDicts(
                collection=replacementsDocsCollection,
                model=ReplacementsFull,
                filter={"_id": ObjectId(replacementsObjId)}
            )[0]

            selectedReplacementsDoc.modifiedGroups.pop(replacementIndex)
            replacementsDocsCollection.update_one(
                filter={"_id": ObjectId(replacementsObjId)},
                update={"$set": {
                    "modifiedGroups": selectedReplacementsDoc.modifiedGroups
                }}
            )
        except HTTPException as e:
            raise HTTPException(e.status_code, e.detail)
        except bson.errors.InvalidId as e:
            raise HTTPException(422, str(e))

        except Exception as e:
            raise HTTPException(500, str(e))


    return router
