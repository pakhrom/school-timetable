from pydantic import BaseModel
from authx import AuthXConfig, AuthX
from pymongo.collection import Collection
from fastapi import APIRouter, HTTPException, Response

from app.BaseModels import CredentialBase
from app.FullModels import UserFull
from hashlib import sha256
from typing import TypedDict

class Security(BaseModel):
    security: AuthX
    config: AuthXConfig

    class Config:
        arbitrary_types_allowed = True

class LoginResponse(TypedDict):
    access_token: str

class LoginRequest(BaseModel):
    username: str
    password: str


def authenticate(
        username: str,
        password: str,
        credentialCollection: Collection,
        userCollection: Collection,
        security: AuthX
) -> str:
    try:
        selectedCredential = credentialCollection.find_one({"username": username})
        selectedUser = UserFull(**userCollection.find_one({"username": username}))
    except TypeError:
        raise HTTPException(404, "User cant be found")
    if not selectedCredential:
        # return {"detail": "No user register", "status_code": 403}
        raise HTTPException(
            detail="No user register",
            status_code=403,
        )

    selectedCredential = CredentialBase(**selectedCredential)
    if selectedCredential.passwordHashed != str(sha256(password.encode('utf-8')).hexdigest()):
        # return {"detail": "Wrong password", "status_code": 401}
        raise HTTPException(
            detail="Wrong password",
            status_code=401,
        )
    if selectedUser.role == "teacher":
        tokenPayload = {
            "role": selectedUser.role,
            "connectedTeacher": selectedUser.connectedTeacher
        }
    else:
        tokenPayload = {
            "role": selectedUser.role
        }

    token = security.create_access_token(
        uid=username, data=tokenPayload
    )
    return token


def createSecurity(JWTSecretKey: str) -> Security:
    authxConfig = AuthXConfig()
    authxConfig.JWT_SECRET_KEY = JWTSecretKey
    # authxConfig.JWT_COOKIE_CSRF_PROTECT = False
    # authxConfig.JWT_ACCESS_COOKIE_NAME = "access_token"
    authxConfig.JWT_TOKEN_LOCATION = ["headers"]

    security = AuthX(authxConfig)
    config_redacted = authxConfig.model_copy()
    config_redacted.JWT_SECRET_KEY = "REDACTED"

    return Security(
        security=security,
        config=config_redacted
    )

def createRouter(
        userCollection: Collection,
        credentialCollection: Collection,
        security: Security,
) -> APIRouter:

    router = APIRouter(
        prefix="/auth",
        tags=["Authorization"]
    )

    @router.post(
        path="/login",
        response_model=LoginResponse
    )
    async def login(credential: LoginRequest):

        token = authenticate(
            username=credential.username,
            password=credential.password,
            credentialCollection=credentialCollection,
            userCollection=userCollection,
            security=security.security
        )
        # response = Response()
        # response.set_cookie(security.config.JWT_ACCESS_COOKIE_NAME, token)
        return LoginResponse(access_token=token)

    return router