from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Annotated
from app.database import get_db_session


SessionDep = Annotated[Session, Depends(get_db_session)]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

AuthDep = Annotated[OAuth2PasswordBearer, Depends(oauth2_scheme)]
