from fastapi import APIRouter
from sqlmodel import select
from app.dependencies import SessionDep
from app.models.imports import User, UserPublic, UserCreate


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/user/me", response_model=UserPublic)
def get_current_user(db_session: SessionDep):
    pass


@router.get("/user/{user_id}", response_model=UserPublic)
def get_user(user_id: int, db_session: SessionDep):
    query = select(User).where(User.id == user_id)

    db_result = db_session.scalar(query)

    result = UserPublic.model_validate(db_result)

    return result


@router.post("/user/", response_model=UserPublic)
def create_user(user: UserCreate, db_session: SessionDep):
    db_user = User.model_validate(user)

    db_session.add(db_user)
    db_session.commit()

    db_session.refresh(db_user)
    
    return db_user


@router.patch("/user/{user_id}", response_model=UserPublic)
def update_user(user_id: int, db_session: SessionDep):
    pass


@router.delete("/user/{user_id}", response_model=UserPublic)
def delete_user(user_id: int, db_session: SessionDep):
    pass

