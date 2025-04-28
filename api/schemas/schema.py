raise DeprecationWarning

from pydantic import BaseModel
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.synchronous.collection import Collection
from config import db_password
from typing import Optional
import BaseModels as dt

_client = MongoClient(f"mongodb+srv://defaultUserAgentBackend:{db_password}@timetableproject.mt2imbb.mongodb.net/?retryWrites=true&w=majority&appName=TimetableProject", server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    _client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
DB = _client.TimetableProject
subjectCollection: Collection = DB["subjects"]
groupsCollection: Collection = DB["groups"]
teachersCollection: Collection = DB["teachers"]
replacementsDocsCollection: Collection = DB["replacementsDocs"]
timetablesCollection: Collection = DB["timetables"]

def getListDicts(collection: Collection, model, **kwargs) -> list[BaseModel]:
    return [
        model(
            objId=str(element.pop("_id")),
            **element
        ) for element in collection.find(**kwargs)
    ]
