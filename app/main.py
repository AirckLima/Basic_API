from dotenv import load_dotenv
import os
from datetime import timedelta
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.routers import users, profiles, posts
from app.database import create_db_and_tables
from app.database import SessionDep
from app.schemas import TokenSchema
from app.lib.verification import get_active_user, authenticate_user, create_access_token

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


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
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    return TokenSchema(access_token=access_token, token_type="bearer")
