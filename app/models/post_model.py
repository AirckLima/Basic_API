from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import TYPE_CHECKING, Union, Optional, List

if TYPE_CHECKING:
    from app.models.profile_model import Profile
    from app.models.user_model import User


class PostBase(SQLModel):
    content: str


class Post(PostBase, table=True):
    id: int = Field(primary_key=True, index=True)
    profile_id: int = Field(foreign_key="profile.id", index=True)

    profile: "User" = Relationship(back_populates="posts")
    

class PostCreate(PostBase):
    profile_id: int
    


class PostPublic(PostBase):
    id: int


class PostUpdate(PostBase):
    pass
