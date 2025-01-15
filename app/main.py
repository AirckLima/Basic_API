from fastapi import FastAPI
from app.routers import users, profiles, posts
from app.database import create_db_and_tables

app = FastAPI(dependencies=[])

app.include_router(users.router)
app.include_router(profiles.router)
app.include_router(posts.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()



@app.get("/")
async def root():
    return {"message": "Welcome to AppDB!"}

