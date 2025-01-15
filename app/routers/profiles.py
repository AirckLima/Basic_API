from fastapi import APIRouter
from app.dependencies import SessionDep
from app.models.imports import Profile, ProfilePublic, ProfileCreate


router = APIRouter(
    prefix="/profiles",
    tags=["profiles"],
    responses={404: {"description": "Not found"}},
)


@router.get("/profile/me", response_model=ProfilePublic)
def get_current_profile(db_session: SessionDep):
    pass


@router.get("/profile/{profile_id}", response_model=ProfilePublic)
def get_profile(profile_id: int, db_session: SessionDep):
    pass


@router.post("/profile/", response_model=ProfilePublic)
def create_profile(profile: ProfileCreate, db_session: SessionDep):
    pass


@router.patch("/profile/{profile_id}", response_model=ProfilePublic)
def update_profile(profile_id: int, db_session: SessionDep):
    pass


@router.delete("/profile/{profile_id}", response_model=ProfilePublic)
def delete_profile(profile_id: int, db_session: SessionDep):
    pass