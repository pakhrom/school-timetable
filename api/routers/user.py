from pydoc import describe

import pymongo.errors
from fastapi import APIRouter, HTTPException
from BaseModels import UserBase, CredentialBase
from FullModels import UserFull, CredentialFull
from pymongo.collection import Collection
from hashlib import sha256

def main(
        userCollection: Collection,
        credentialCollection: Collection,
) -> APIRouter:

    router = APIRouter(
        prefix="/users",
        tags=["User"]
    )

    @router.get(
        path="/{username}",
        response_model=UserFull
    )
    async def getUser(username: str):
        return UserFull(
            **userCollection.find_one({"username": username})
        )


    @router.post(
        path="",
        # response_model=...
    )
    async def createUser(user: UserBase, password: str):
        try:
            credentialCollection.insert_one(
                CredentialFull(
                    username=user.username,
                    passwordHashed=str(sha256(password.encode('utf-8')).hexdigest())
                ).model_dump(exclude=["objId"])
            )
            userCollection.insert_one(user.model_dump(exclude=["objId"]))
            # TODO: Add JWT token return
        except pymongo.errors.DuplicateKeyError:
            raise HTTPException(
                status_code=409,
                detail="User already exist"
            )

    @router.delete(
        path="/{username}",
        response_model=int,
    )
    async def deleteUser(username: str):
        credentialCollection.delete_one({"username": username})
        userCollection.delete_one({"username": username})

    return router