from fastapi import APIRouter
from app.dependencies import SessionDep
from app.models.imports import Post, PostPublic, PostCreate

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.get("/post/{post_id}", response_model=PostPublic)
def get_post(post_id: int, db_session: SessionDep):
    pass


@router.post("/post/", response_model=PostPublic)
def create_post(post: Post, db_session: SessionDep):
    pass


@router.patch("/post/{post_id}", response_model=PostPublic)
def update_post(post_id: int, db_session: SessionDep):
    pass


@router.delete("/post/{post_id}", response_model=PostPublic)
def delete_post(post_id: int, db_session: SessionDep):
    pass