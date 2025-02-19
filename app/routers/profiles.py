from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.database import SessionDep
from app.models import  Profile as ProfileModel
from app.schemas import ProfileSchema, ProfileCreateSchema, ProfileUpdateSchema

router = APIRouter(
    prefix="/profiles",
    tags=["profiles"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{profile_id}", response_model=ProfileSchema)
def get_profile(profile_id: int, db_session: SessionDep):
    query = select(ProfileModel).where(ProfileModel.id == profile_id)

    db_result = db_session.scalar(query)
    
    if not db_result:
        raise HTTPException(status_code=404, detail="Entity not found")
    
    result = ProfileSchema.model_validate(db_result).model_dump()
    
    return result


@router.post("/", response_model=ProfileSchema)
def create_profile(profile: ProfileCreateSchema, db_session: SessionDep):
    db_profile = ProfileModel(**profile.model_dump())
    
    db_session.add(db_profile)
    db_session.commit()
    db_session.refresh(db_profile)
    
    return db_profile


@router.patch("/{profile_id}", response_model=ProfileSchema)
def update_profile(profile_id: int, patch_profile: ProfileUpdateSchema, db_session: SessionDep):
    query = select(ProfileModel).where(ProfileModel.id == profile_id)
    
    db_result = db_session.scalar(query)

    if not db_result:
        raise HTTPException(status_code=404, detail="Entity not found")
    
    update_data =  patch_profile.model_dump(exclude_unset=True)

    db_result.sqlmodel_update(update_data)

    db_session.add(db_result)
    db_session.commit()
    db_session.refresh(db_result)

    print(update_data)
    
    return db_result

@router.delete("/{profile_id}")
def delete_profile(profile_id: int, db_session: SessionDep):
    query = select(ProfileModel).where(ProfileModel.id == profile_id)
    
    db_result = db_session.scalar(query)

    if not db_result:
        raise HTTPException(status_code=404, detail="Entity not found")
    
    db_session.delete(db_result)
    db_session.commit()

    return {"msg": f"Entity {ProfileSchema.__name__}-ID{db_result.id} has been deleted."}