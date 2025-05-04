from pydantic import BaseModel
from authx import AuthXConfig, AuthX
from pymongo.collection import Collection
from fastapi import APIRouter, HTTPException, Response

import config
from BaseModels import CredentialBase
from hashlib import sha256
from typing import TypedDict

class Security(BaseModel):
    security: AuthX
    config: AuthXConfig

    class Config:
        arbitrary_types_allowed = True

def createSecurity(JWTSecretKey: str) -> Security:
    authxConfig = AuthXConfig()
    authxConfig.JWT_SECRET_KEY = JWTSecretKey
    authxConfig.JWT_ACCESS_COOKIE_NAME = "access_token"
    authxConfig.JWT_TOKEN_LOCATION = ["cookies"]

    security = AuthX(authxConfig)
    config_redacted = authxConfig.model_copy()
    config_redacted.JWT_SECRET_KEY = "REDACTED"

    return Security(
        security=security,
        config=config_redacted
    )

def createRouter(credentialCollection: Collection, security: Security) -> APIRouter:

    router = APIRouter(
        prefix="/auth",
        tags=["Authorization"]
    )

    class LoginResponse(TypedDict):
        access_token: str

    class LoginRequest(BaseModel):
        username: str
        password: str

    @router.post(
        path="/login",
        response_model=LoginResponse
    )
    async def login(credential: LoginRequest, response: Response):
        password = credential.password
        username = credential.username
        selectedCredential = credentialCollection.find_one({"username": username})
        if not selectedCredential:
            raise HTTPException(
                status_code=404,
                detail="No such user"
            )

        selectedCredential = CredentialBase(**selectedCredential)
        if selectedCredential.passwordHashed != str(sha256(password.encode('utf-8')).hexdigest()):
            raise HTTPException(
                status_code=401,
                detail="Wrong password"
            )
        token = security.security.create_access_token(
            uid=username
        )
        response.set_cookie(security.config.JWT_ACCESS_COOKIE_NAME, token)
        return LoginResponse(access_token=token)

    return router