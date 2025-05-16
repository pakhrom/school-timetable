import authx.exceptions
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import PlainTextResponse

import app.FullModels
from app.schemas.DBLoad import DBLoad
from app.config import mongoDBURL, JWTSecretKey
from app.auth import authentication
import uvicorn
import app.routers as routers

from pydantic import BaseModel
from bson import ObjectId

app = FastAPI(title="api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB init
mongoDB = DBLoad(
    host=mongoDBURL
)

# Security init
security = authentication.createSecurity(JWTSecretKey)
security.security.handle_errors(app)
app.include_router(
    authentication.createRouter(
        userCollection=mongoDB.usersCollection,
        credentialCollection=mongoDB.credentialCollection,
        security=security,
    )
)

# Work objects init
app.include_router(
    routers.timetable.main(
        mongoDB.timetablesCollection,
        security.security
    )
)
app.include_router(
    routers.teacher.main(
        mongoDB.teachersCollection,
        security.security
    )
)
app.include_router(
    routers.subject.main(
        mongoDB.subjectCollection,
        security.security
    )
)
app.include_router(
    routers.replacements.main(
        mongoDB.replacementsDocsCollection,
        mongoDB.groupsCollection,
        security.security
    )
)
app.include_router(
    routers.group.main(
        groupsCollection=mongoDB.groupsCollection,
        security=security.security,
        teacherCollection=mongoDB.teachersCollection,
        subjectsCollection=mongoDB.subjectCollection
    )
)
# app.include_router(
#     routers.callSchedule.main(
#         mongoDB.callSchedulesCollection,
#         security.security
#     )
# )
app.include_router(
    routers.user.main(mongoDB.usersCollection, mongoDB.credentialCollection, security.security)
)
# No authorization cookie error processing
# @app.exception_handler(authx.exceptions.MissingTokenError)
async def NoAuthCookie(request, exc):
    return PlainTextResponse(
        str(exc), status_code=403
    )

# Expired auth cookie
# @app.exception_handler(authx.exceptions.JWTDecodeError)
async def OldCookie(request, exc):
    return PlainTextResponse(
        str(exc), status_code=401
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=8080
    )
