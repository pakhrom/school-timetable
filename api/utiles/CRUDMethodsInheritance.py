raise DeprecationWarning

from fastapi import APIRouter
from schemas.schema import getListDicts
from bson.objectid import ObjectId
from pymongo import collection

def CRUDMethods(
        router: APIRouter,
        responseBodyClass,
        requestBodyClass,
        mongoCollection: collection,
        excludedFields: list[str] = ("objId")
):
    @router.get(
        path="",
        response_model=list[responseBodyClass],
        description="Get list of full objects Subject"
    )
    async def all() -> list[responseBodyClass]:
        return getListDicts(
            collection = mongoCollection,
            model = responseBodyClass,
        )



    @router.post(
        path="",
        response_model=str,
    )
    async def add(obj: requestBodyClass):
        result = mongoCollection.insert_one(
            obj.model_dump(exclude=excludedFields)
        )
        return str(result.inserted_id)

    @router.put(
        path="/{objId}",
    )
    async def update(objId: str, obj: requestBodyClass):
        obj.objId = objId
        result = mongoCollection.update_one(
            filter={"_id": ObjectId(objId)},
            update={"$set": obj.model_dump()}
        )
        return str(result.raw_result)

    @router.delete(
        path="/{objId}"
    )
    async def delete(objId: str):
        result = mongoCollection.delete_one(
            filter={"_id": ObjectId(objId)},
        )
        return str(result.raw_result)

