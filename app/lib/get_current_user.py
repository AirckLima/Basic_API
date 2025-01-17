from sqlalchemy import select
from app.models import User
from app.schemas import UserDBSchema
from app.dependencies import SessionDep, TokenDep


def get_current_user(db_session: SessionDep, token: TokenDep) -> UserDBSchema:
    query = select(User).where(User.username == token)
    
    user_data = db_session.scalar(query)

    return UserDBSchema.model_validate(user_data)



