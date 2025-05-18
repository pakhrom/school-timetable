from fastapi import APIRouter, Depends, HTTPException, Header

from app.BaseModels import GroupBase
from app.FullModels import GroupFull, SubjectFull, TeacherFull

from pymongo.collection import Collection
from authx import AuthX, TokenPayload, RequestToken
from typing import Annotated
from typing_extensions import TypedDict
from app.schemas.DBLoad import getListDicts
from bson.objectid import ObjectId
from app.utiles.dataPreprocessing import processForDB
from enum import Enum
from pydantic import BaseModel, ConfigDict


def main(
        groupsCollection: Collection,
        security: AuthX,
        teachersCollection: Collection,
        subjectsCollection: Collection,
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

    class groupBy(str, Enum):
        none = "none"
        subjects = "subjects"
        teachers = "teachers"
        # className = "className"

    @router.get(
        path="",
        # response_model=list[GroupFull]
    )
    async def GetAll(
            groupBy: groupBy = groupBy.none,
    ):
        if groupBy == groupBy.none:
            return getListDicts(
                collection=groupsCollection,
                model=GroupFull,
                modelLambda= lambda x: x.printOut(
                    subjectsCollection=subjectsCollection,
                    teacherCollection=teachersCollection
                )
            )
        else:
            if groupBy == groupBy.subjects:
                keyValue = "$subjectId"
            elif groupBy == groupBy.teachers:
                keyValue = "$teacherId"
            else:
                raise HTTPException(422, "Wrong grouping")

            pipeline = [
                {"$group": {
                    "_id": keyValue,
                    "items": {"$push": "$$ROOT"}
                }}
            ]

            cursor = groupsCollection.aggregate(pipeline)
            response = {
                str(doc["_id"]): [
                    GroupFull(**el).printOut(
                        subjectsCollection=subjectsCollection,
                        teacherCollection=teachersCollection,
                    ) for el in doc["items"]
                ] for doc in cursor
            }
            return response

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
        if not group.verify_dependencies(
            teachersCollection=teachersCollection,
            subjectsCollection=subjectsCollection,
        ):
            raise HTTPException(422, "Can`t verify group dependencies")
        response = groupsCollection.insert_one(processForDB(
            baseObject=group,
            fullModel=GroupFull
        ))

        GroupBase.pairGroup(
            collection=[
                subjectsCollection,
                teachersCollection,
            ],
            addId=str(response.inserted_id),
            selectId=[
                group.subjectId,
                group.teacherId
            ]
        )

        return ObjectId(response.inserted_id)

    @router.put(
        path="/{objId}",
        dependencies=[Depends(authorization)]
    )
    async def UpdateOne(objId: str, group: GroupBase):
        if not group.verify_dependencies(
                teachersCollection=teachersCollection,
                subjectsCollection=subjectsCollection,
        ):
            raise HTTPException(422, "Can`t verify group dependencies")

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

        group: GroupFull = getListDicts(
            collection=groupsCollection,
            model=GroupFull,
            filter={"_id": ObjectId(objId)}
        )[0]

        GroupBase.unpairGroup(
            collection=[
                subjectsCollection,
                teachersCollection,
            ],
            delId=objId,
            selectId=[
                group.subjectId,
                group.teacherId
            ]
        )

        response = groupsCollection.delete_one({"_id": ObjectId(objId)})

        if response.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Group not found")

    return router