from app.schemas import User
from app.dependencies import SessionDep, AuthDep


def get_current_user(token: AuthDep) -> User:
    return User()



