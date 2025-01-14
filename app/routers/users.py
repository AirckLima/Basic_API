from fastapi import APIRouter
from app.dependencies import SessionDep
from app.models import user_model as User, profile_model as Profile, post_model as Post


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/user/me", response_model=User.UserPublic)
def get_current_user(db_session: SessionDep):
    pass


@router.get("/user/{user_id}", response_model=User.UserPublic)
def get_user(user_id: int, db_session: SessionDep):
    pass


@router.post("/user/{user_id}", response_model=User.UserPublic)
def create_user(user_id: int, db_session: SessionDep):
    pass


@router.patch("/user/{user_id}", response_model=User.UserPublic)
def update_user(user_id: int, db_session: SessionDep):
    pass


@router.delete("/user/{user_id}", response_model=User.UserPublic)
def delete_user(user_id: int, db_session: SessionDep):
    pass

