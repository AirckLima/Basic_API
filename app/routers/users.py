from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from typing import Annotated, Any
from app.dependencies import SessionDep, AuthDep
from app.models import  User as UserModel
from app.schemas import User, UserResponse, UserCreate, UserUpdate
from app.lib.get_current_user import get_current_user
from app.lib.get_active_user import get_active_user


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/me", response_model=UserResponse)
def get_current_user(current_user: Annotated[User, Annotated[User, Depends(get_active_user)]], db_session: SessionDep):
    return current_user


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db_session: SessionDep):
    query = select(UserModel).where(UserModel.id == user_id)

    db_result = db_session.scalar(query)
    
    if not db_result:
        raise HTTPException(status_code=404, detail="Entity not found")
    
    result = UserResponse.model_validate(db_result)

    return result


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db_session: SessionDep):
    db_user = User.model_validate(user)
    
    db_session.add(db_user)
    db_session.commit()
    db_session.refresh(db_user)
    
    return db_user


@router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, patch_user: UserUpdate, db_session: SessionDep):
    query = select(UserModel).where(UserModel.id == user_id)
    
    db_result = db_session.scalar(query)

    if not db_result:
        raise HTTPException(status_code=404, detail="Entity not found")
    
    update_data =  patch_user.model_dump(exclude_unset=True)

    db_result.sqlmodel_update(update_data)

    db_session.add(db_result)
    db_session.commit()
    db_session.refresh(db_result)

    print(update_data)
    
    return db_result


@router.delete("/{user_id}")
def delete_user(user_id: int, db_session: SessionDep):
    query = select(UserModel).where(UserModel.id == user_id)
    
    db_result = db_session.scalar(query)

    if not db_result:
        raise HTTPException(status_code=404, detail="Entity not found")
    
    db_session.delete(db_result)
    db_session.commit()

    return {"msg": f"Entity {User.__name__}-ID{db_result.id} has been deleted."}

