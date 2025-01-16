from typing import Annotated

from fastapi import Depends

from app.schemas import User
# from app.dependencies import SessionDep, AuthDep
from .get_current_user import get_current_user


def get_active_user(token: Annotated[User, Depends(get_current_user)]) -> User:
    return User()



