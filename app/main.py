
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
from app.lib.verification import get_active_user, get_password_hash, authenticate_user, create_access_token



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

    user = authenticate_user(db_session, form_data.username, form_data.password)

    return { "access_token": user.username, "token_type": "bearer" }