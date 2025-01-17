from dotenv import load_dotenv
import os
from sqlalchemy import select
from app.models import User
from app.schemas import UserDBSchema
from app.dependencies import SessionDep, TokenDep
# from app.lib
from datetime import datetime, timedelta
from time import timezone
from passlib.context import CryptContext
from fastapi import Depends
from typing import Annotated
import jwt

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_current_user(db_session: SessionDep, token: TokenDep) -> UserDBSchema:
    query = select(User).where(User == token)
    
    user_data = db_session.scalar(query)

    return UserDBSchema.model_validate(user_data)


def get_active_user(current_user: Annotated[UserDBSchema, Depends(get_current_user)]) -> UserDBSchema:
    return current_user


def verify_password(pwd_context: CryptContext, plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(pwd_context: CryptContext, password):
    return pwd_context.hash(password)


def authenticate_user(db_session: SessionDep, username: str, password: str):
    query = select(User).where(User.username == username)

    user_db = db_session.scalar(query)

    if not user_db:
        return False
    if not verify_password(password, user_db.hashed_password):
        return False
    
    user = UserDBSchema.model_validate(user_db)

    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt