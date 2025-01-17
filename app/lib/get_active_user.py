from typing import Annotated

from fastapi import Depends

from app.schemas import UserDBSchema, UserSchema
# from app.dependencies import SessionDep, AuthDep
from .get_current_user import get_current_user


def get_active_user(current_user: Annotated[UserDBSchema, Depends(get_current_user)]) -> UserDBSchema:
    return current_user


AuthDep = Annotated[UserDBSchema, Depends(get_active_user)]
