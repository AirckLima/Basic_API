from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.dependencies import SessionDep
from app.models import  Post as PostModel
from app.schemas import PostSchema, PostCreateSchema, PostUpdateSchema


router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{post_id}", response_model=PostSchema)
def get_post(post_id: int, db_session: SessionDep):
    query = select(PostModel).where(PostModel.id == post_id)

    db_result = db_session.scalar(query)
    
    if not db_result:
        raise HTTPException(status_code=404, detail="Entity not found")
    
    result = PostSchema.model_validate(db_result)

    return result


@router.post("/", response_model=PostSchema)
def create_post(post: PostCreateSchema, db_session: SessionDep):
    db_post = PostModel(**post.model_dump())
    
    db_session.add(db_post)
    db_session.commit()
    db_session.refresh(db_post)
    
    return db_post


@router.patch("/{post_id}", response_model=PostSchema)
def update_post(post_id: int, patch_post: PostUpdateSchema, db_session: SessionDep):
    query = select(PostModel).where(PostModel.id == post_id)
    
    db_result = db_session.scalar(query)

    if not db_result:
        raise HTTPException(status_code=404, detail="Entity not found")
    
    update_data =  patch_post.model_dump(exclude_unset=True)

    db_result.sqlmodel_update(update_data)

    db_session.add(db_result)
    db_session.commit()
    db_session.refresh(db_result)

    print(update_data)
    
    return db_result


@router.delete("/{post_id}")
def delete_post(post_id: int, db_session: SessionDep):
    query = select(PostModel).where(PostModel.id == post_id)
    
    db_result = db_session.scalar(query)

    if not db_result:
        raise HTTPException(status_code=404, detail="Entity not found")
    
    db_session.delete(db_result)
    db_session.commit()

    return {"msg": f"Entity {PostSchema.__name__}-ID{db_result.id} has been deleted."}