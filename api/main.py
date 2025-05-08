import authx.exceptions
from fastapi import FastAPI
from starlette.responses import PlainTextResponse

import app.FullModels
from app.schemas.DBLoad import DBLoad
from app.config import mongoDBURL, JWTSecretKey
from app.auth import authentication
import uvicorn
import app.routers as routers


app = FastAPI(title="api")

# DB init
mongoDB = DBLoad(
    host=mongoDBURL
)

# Security init
security = auth.createSecurity(JWTSecretKey)
app.include_router(
    auth.createRouter(
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
        security.security
    )
)
app.include_router(
    routers.group.main(
        mongoDB.groupsCollection,
        security.security
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
@app.exception_handler(authx.exceptions.MissingTokenError)
async def NoAuthCookie(request, exc):
    return PlainTextResponse(
        str(exc), status_code=403
    )

# Expired auth cookie
@app.exception_handler(authx.exceptions.JWTDecodeError)
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
