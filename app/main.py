from dotenv import load_dotenv
import os
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from app.routers import users, profiles, posts
from app.database import create_db_and_tables
from app.models import User
from app.schemas import UserDBSchema
from app.dependencies import SessionDep
from app.lib.get_active_user import AuthDep, get_active_user

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI(dependencies=[])

app.include_router(users.router, dependencies=[Depends(get_active_user)])
app.include_router(profiles.router, dependencies=[Depends(get_active_user)])
app.include_router(posts.router, dependencies=[Depends(get_active_user)])


@app.on_event("startup")
def on_startup():
    create_db_and_tables()



@app.get("/")
async def root():
    return {"message": "Welcome to AppDB!"}


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db_session: SessionDep):
    query = select(User).where(User.username == form_data.username)

    user_db = db_session.scalar(query)

    if not user_db:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    user = UserDBSchema.model_validate(user_db)

    password = form_data.password

    if not password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return { "access_token": user.username, "token_type": "bearer" }