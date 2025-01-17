from sqlalchemy import select
from app.models import User
from app.schemas import UserDBSchema
from app.dependencies import SessionDep



def get_user_by_id(db_session:SessionDep, user_id:int):
    query = select(User).where(User.id == user_id)

    user_db = db_session.scalar(query)


def get_user_by_username(db_session:SessionDep, username:int):
    query = select(User).where(User.username == username)

    user_db = db_session.scalar(query)

