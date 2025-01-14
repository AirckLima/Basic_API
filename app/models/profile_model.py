from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import TYPE_CHECKING, Union, Optional, List

if TYPE_CHECKING:
    from .user_model import User, UserPublic
    from .post_model import Post, PostPublic


class ProfileBase(SQLModel):
    nickname: str = Field(index=True)
    avatar: str | None = Field(default=None)
    bio: str | None = Field(default=None)


class Profile(ProfileBase, table=True):
    id: int = Field(primary_key=True, index=True)
    user_id: int = Field(foreign_key="user.id", index=True)

    user: "User" = Relationship()
    posts: List["User"] = Relationship(back_populates="profile")


class ProfileCreate(ProfileBase):
    user_id: int


class ProfilePublic(ProfileBase):
    id: int
    user: "UserPublic"
    posts: List["PostPublic"]


class ProfileUpdate(ProfileBase):
    pass