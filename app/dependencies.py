from fastapi import Depends
from sqlmodel import Session
from typing import Annotated
from app.database import engine, get_db_session


SessionDep = Annotated[Session, Depends(get_db_session)]