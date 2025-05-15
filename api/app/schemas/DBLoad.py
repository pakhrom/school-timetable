import logging
from enum import unique

from anyio.to_process import current_default_process_limiter
from bson import ObjectId
from fastapi import HTTPException
from typing import TypeVar

import pymongo
from pydantic import BaseModel
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.synchronous.collection import Collection


class DBLoad:
    def __init__(
            self,
            host: str
    ):
        self.host = host
        client = MongoClient(
            host=self.host,
            server_api=ServerApi('1'),
        )
        logger = logging.getLogger("uvicorn.debug")
        try:
            client.admin.command('ping')
            logger.info(
                msg="Pinged your deployment. You successfully connected to MongoDB!",
            )

            self.DB = client.TimetableProject
            self.subjectCollection: Collection = self.DB["subjects"]
            self.groupsCollection: Collection = self.DB["groups"]
            self.teachersCollection: Collection = self.DB["teachers"]
            self.replacementsDocsCollection: Collection = self.DB["replacementsDocs"]
            self.timetablesCollection: Collection = self.DB["timetables"]
            self.callSchedulesCollection: Collection = self.DB["callSchedules"]

            self.usersCollection: Collection = self.DB["users"]
            self.usersCollection.create_index("username", unique=True)

            self.credentialCollection: Collection = self.DB["credentials"]
            self.credentialCollection.create_index("username", unique=True)

        except pymongo.mongo_client.ConnectionFailure as e:
            logger.error(
                msg=f"Cant connect to mongoDB:\n{e}"
            )

def getListDicts(collection: Collection, model, **kwargs) -> list:

    response = [
        model(
            objId=str(element.pop("_id")),
            **element
        ) for element in collection.find(**kwargs)
    ]
    if len(response) == 0 and "filter" in kwargs.keys():
        raise HTTPException(404, f"Element {model.__name__} can`t be found")
    return response