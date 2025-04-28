from fastapi import APIRouter
from pydantic import BaseModel
from schemas.DBLoad import getListDicts
from bson.objectid import ObjectId
from pymongo import collection

class CRUDMethods:
    kwargsAdd: dict = {}
    kwargsUpdate: dict = {}
    kwargsDelete: dict = {}
    kwargsGetOne: dict = {}
    kwargsGetAll: dict = {}
    systemDBFields: list[str] = ("objId")
    def __init__(
            self,
            router: APIRouter,
            fullModel,
            baseModel,
            mongoCollection: collection,
    ):
        self.router = router
        self.fullModel = fullModel
        self.baseModel = baseModel
        self.mongoCollection = mongoCollection

    def  GetOne(self):
        @self.router.get(
            path="/{objId}",
            response_model=self.fullModel,
            description="Get one object Subject by objId"
        )
        async def one(objId: str):
            response = getListDicts(
                collection=self.mongoCollection,
                model=self.fullModel,
                filter={"_id": ObjectId(objId)}
            )
            try:
                return response[0]
            except IndexError:
                raise IndexError(f"Obj with Id: {objId} can`t be found")

    def GetAll(self):
        fullModel = self.fullModel
        class ListResponseModel(BaseModel):
            data: list[fullModel]
        @self.router.get(
            path="",
            response_model=ListResponseModel,
            description="Get list of full objects Subject"
        )
        async def all():
            return ListResponseModel(
                data=getListDicts(
                    collection=self.mongoCollection,
                    model=self.fullModel,
                )
            )

    def AddOne(self):
        baseModel = self.baseModel
        @self.router.post(
            path="",
            response_model=str,
        )
        async def add(obj: baseModel):
            result = self.mongoCollection.insert_one(
                self.fullModel(
                    **obj.model_dump()
                ).model_dump(exclude=self.systemDBFields)
            )
            return str(result.inserted_id)

    def UpdateOne(self):
        baseModel = self.baseModel
        @self.router.put(
            path="/{objId}",
        )
        async def update(objId: str, obj: baseModel):
            obj.objId = objId
            result = self.mongoCollection.update_one(
                filter={"_id": ObjectId(objId)},
                update={
                    "$set": self.fullModel(**obj).model_dump(exclude=self.systemDBFields)
                }
            )
            return str(result.raw_result)

    def DeleteOne(self):
        @self.router.delete(
            path="/{objId}"
        )
        async def delete(objId: str):
            result = self.mongoCollection.delete_one(
                filter={"_id": ObjectId(objId)},
            )
            return str(result.raw_result)

    def SetupMethods(
            self,
    ):
        self.AddOne()
        self.DeleteOne()
        self.GetAll()
        self.GetOne()
        self.UpdateOne()

