from fastapi import APIRouter, HTTPException, Depends, Response
from pydantic import BaseModel, ConfigDict
from pymongo.errors import DuplicateKeyError
from starlette.responses import RedirectResponse


from app.BaseModels import UserBase
from app.FullModels import UserFull, CredentialFull
from app.auth.authentication import authenticate, LoginResponse

from pymongo.collection import Collection
from hashlib import sha256

from authx import AuthX

class PasswordRequestForm(BaseModel):
    password: str

def main(
        userCollection: Collection,
        credentialCollection: Collection,
        security: AuthX
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
        user_data = userCollection.find_one({"username": username})
        if user_data is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        return UserFull(**user_data)


    @router.post(
        path="",
        response_model = dict,
        # dependencies=[Depends(security.get_token_from_request)]
    )
    async def createUser(user: UserBase, password: PasswordRequestForm):
            try:
                credentialCollection.insert_one(
                    CredentialFull(
                        username=user.username,
                        passwordHashed=str(sha256(password.password.encode('utf-8')).hexdigest())
                    ).model_dump(exclude={"objId"})
                )
                userCollection.insert_one(user.model_dump(exclude={"objId"}))

                token = authenticate(
                    username=user.username,
                    password=password.password,
                    userCollection=userCollection,
                    credentialCollection=credentialCollection,
                    security=security,
                )

                # response.set_cookie(security.config.JWT_ACCESS_COOKIE_NAME, token)
                return LoginResponse(access_token=token)

            except DuplicateKeyError:
                raise HTTPException(
                    status_code=409,
                    detail="User already exist"
                )

    @router.delete(
        path="/{username}",
        dependencies=[Depends(security.get_token_from_request)]
    )
    async def deleteUser(username: str):
        credentialCollection.delete_one({"username": username})
        userCollection.delete_one({"username": username})

    return router
