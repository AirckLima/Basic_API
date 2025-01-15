from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import TYPE_CHECKING, Union, Optional, List

if TYPE_CHECKING:
    from app.models.profile_model import Profile, ProfilePublic


class PostBase(SQLModel):
    content: str


class Post(PostBase, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    profile_id: int = Field(foreign_key="profile.id", index=True)

    profile: "Profile" = Relationship(back_populates="posts")
    

class PostCreate(PostBase):
    profile_id: int
    

class PostPublic(PostBase):
    id: int

    profile: "ProfilePublic"


class PostUpdate(PostBase):
    pass


# https://github.com/fastapi/sqlmodel/discussions/757#discussioncomment-9602092

from app.models.profile_model import Profile, ProfilePublic

ProfilePublic.model_rebuild()