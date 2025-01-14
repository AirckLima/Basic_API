from fastapi import APIRouter
from app.dependencies import SessionDep
from app.models import user_model as User, profile_model as Profile, post_model as Post


router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.get("/post/{post_id}", response_model=Post.PostPublic)
def get_post(post_id: int, db_session: SessionDep):
    pass


@router.post("/post/{post_id}", response_model=Post.PostPublic)
def create_post(post_id: int, db_session: SessionDep):
    pass


@router.patch("/post/{post_id}", response_model=Post.PostPublic)
def update_post(post_id: int, db_session: SessionDep):
    pass


@router.delete("/post/{post_id}", response_model=Post.PostPublic)
def delete_post(post_id: int, db_session: SessionDep):
    pass