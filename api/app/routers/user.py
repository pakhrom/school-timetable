import logging
from http.client import responses
from typing import Optional, TypedDict

from fastapi import APIRouter, HTTPException, Depends, Response, Header
from pydantic import BaseModel, ConfigDict, Field
from pymongo.errors import DuplicateKeyError
from starlette.responses import RedirectResponse


from app.BaseModels import UserBase, UserRole, PyObjectId, ResponseCount
from app.FullModels import UserFull, CredentialFull
from app.auth.authentication import authenticate, LoginResponse

from pymongo.collection import Collection
from hashlib import sha256

from bson import ObjectId

from authx import AuthX, RequestToken

class PasswordRequestForm(BaseModel):
    password: str = Field(min_length=10, max_length=50)

def main(
        userCollection: Collection,
        credentialCollection: Collection,
        teachersCollection: Collection,
        security: AuthX,
) -> APIRouter:
    def Only_admins(
            token: str = Header(),
    ) -> bool:
        JWTData = security.verify_token(RequestToken(
            token=token,
            location="headers"
        ))
        if JWTData.role != "admin":
            raise HTTPException(
                status_code=403,
                detail="Only admins can edit subjects"
            )
        return True

    class TokenPayload(BaseModel):
        username: str
        role: UserRole

    def Only_user_itself(
            token: str = Header(),
    ) -> TokenPayload:
        JWTData = security.verify_token(RequestToken(
            token=token,
            location="headers"
        ))
        return TokenPayload(
            username=JWTData.sub,
            role=JWTData.role
        )

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
        dependencies=[Depends(Only_admins)]
    )
    async def createUser(user: UserBase, password: PasswordRequestForm):
            try:
                logger = logging.getLogger("uvicorn.debug")
                logger.info(user.connectedTeacher)
                logger.info(str(teachersCollection.find_one({"_id": ObjectId(user.connectedTeacher)})))

                if not user.verify_teacher(
                        teachersCollection=teachersCollection
                ):
                    raise HTTPException(422, "Connected teacher can`t be found")

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

    class UserUpdatePayload(BaseModel):
        displayName: Optional[str] = None
        role: Optional[UserRole] = None
        connectedTeacher: Optional[PyObjectId] = None


    @router.put(
        path="/{username}",
        response_model=ResponseCount,
    )
    async def updateUser(username: str, UpdatePayload: UserUpdatePayload, tokenPayload: TokenPayload = Depends(Only_user_itself)):
        if tokenPayload.username != username and tokenPayload.role != "admin":
            raise HTTPException(403, "God forbid, Dianne")
        user = UserFull(**userCollection.find_one({"username": username}))
        if UpdatePayload.role and user.role != UpdatePayload.role:
            if user.role == "teacher" and UpdatePayload.role == "admin":
                raise HTTPException(403, "No rights?")
            user.role = UpdatePayload.role
        if UpdatePayload.displayName and user.displayName != UpdatePayload.displayName:
            user.displayName = UpdatePayload.displayName
        if UpdatePayload.connectedTeacher and user.connectedTeacher != UpdatePayload.connectedTeacher:
            user.connectedTeacher = UpdatePayload.connectedTeacher

        if not user.verify_teacher(
            teachersCollection=teachersCollection
        ):
            raise HTTPException(422, "Connected teacher can`t be found")

        user.model_validate(user)

        return ResponseCount(
            count=userCollection.update_one({"username": username},
                                            {"$set": user.model_dump(exclude={"_id", "username"})}).modified_count
        )

    class UpdateUserPasswordPayload(BaseModel):
        oldPassword: str = Field(min_length=10)
        newPassword: str = Field(min_length=10)

    @router.put(
        path="/{username}/update_password",
        response_model=ResponseCount,
    )
    def UpdateUserPassword(
            username: str,
            passwordPayload: UpdateUserPasswordPayload,
            tokenPayload: TokenPayload = Depends(Only_user_itself)
    ):
        if username != tokenPayload.username and tokenPayload.role != "admin":
            raise HTTPException(403, "You shall not pass! - Gendalf")
        creds = CredentialFull(**credentialCollection.find_one({"username": username}))
        if not creds.passwordHashed == str(sha256(passwordPayload.oldPassword.encode('utf-8')).hexdigest()):
            raise HTTPException(403, "Ты куда собрался, полурослик?")
        creds.passwordHashed = str(sha256(passwordPayload.newPassword.encode('utf-8')).hexdigest())

        return ResponseCount(
            count=credentialCollection.update_one({"username": username}, {"$set": creds.model_dump(exclude={"_id", "username"})}).modified_count
        )

    @router.delete(
        path="/{username}",
        dependencies=[Depends(Only_admins)],
    )
    async def deleteUser(username: str):
        credentialCollection.delete_one({"username": username})
        userCollection.delete_one({"username": username})

    return router
