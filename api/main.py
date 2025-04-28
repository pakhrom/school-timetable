from fastapi import FastAPI
from schemas.DBLoad import DBLoad
from config import db_password
import uvicorn
import routers
from uvicorn import logging

app = FastAPI(title="api")

mongoDB = DBLoad(
    host=f"mongodb+srv://defaultUserAgentBackend:{db_password}@timetableproject.mt2imbb.mongodb.net/?retryWrites=true&w=majority&appName=TimetableProject"
)


app.include_router(
    routers.timetable.main(mongoDB.timetablesCollection)
)
app.include_router(
    routers.teacher.main(mongoDB.teachersCollection)
)
app.include_router(
    routers.subject.main(mongoDB.subjectCollection)
)
app.include_router(
    routers.replacements.main(mongoDB.replacementsDocsCollection)
)
app.include_router(
    routers.group.main(mongoDB.groupsCollection)
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True
    )