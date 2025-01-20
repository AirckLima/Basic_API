from typing import Annotated
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os
from sqlalchemy import select
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError
from app.database import SessionDep
from app.models import User
from app.schemas import UserDBSchema, TokenDataSchema, UserSchema

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated=["auto"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

TokenDep = Annotated[OAuth2PasswordBearer, Depends(oauth2_scheme)]


def get_current_user(db_session: SessionDep, token: TokenDep) -> UserDBSchema:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        username = payload.get("sub")
        
        if username is None:
            raise credentials_exception

        token_data = TokenDataSchema(username=username)

    except InvalidTokenError:
        raise credentials_exception

    query = select(User).where(User.username == token_data.username)
    
    user_data = db_session.scalar(query)

    if user_data is None:
        raise credentials_exception

    return UserDBSchema.model_validate(user_data)


def get_active_user(current_user: Annotated[UserDBSchema, Depends(get_current_user)]) -> UserDBSchema:
    return current_user


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
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


AuthDep = Annotated[UserSchema, Depends(get_active_user)]
