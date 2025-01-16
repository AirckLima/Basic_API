from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from app.routers import users, profiles, posts
from app.database import create_db_and_tables
from app.models import User
from app.schemas import UserDB

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


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_db = select(User).where(User.username == form_data.username)

    if not user_db:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    user = UserDB(**user_db)

    password = "fake" + form_data.password

    if not password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return { "access_token": user.username, "token_type": "bearer" }