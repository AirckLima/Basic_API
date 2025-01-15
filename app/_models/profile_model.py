from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import TYPE_CHECKING, Union, Optional, List

if TYPE_CHECKING:
    from app.models.user_model import User, UserPublic
    from app.models.post_model import Post, PostPublic


class ProfileBase(SQLModel):
    nickname: str = Field(index=True)
    avatar: str | None = Field(default=None)
    bio: str | None = Field(default=None)


class Profile(ProfileBase, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    user_id: int = Field(foreign_key="user.id", index=True)

    user: "User" = Relationship()
    posts: list["Post"] = Relationship(back_populates="profile")


class ProfileCreate(ProfileBase):
    user_id: int


class ProfilePublic(ProfileBase):
    id: int
    user: "UserPublic"
    posts: list["PostPublic"]


class ProfileUpdate(ProfileBase):
    pass

# https://github.com/fastapi/sqlmodel/discussions/757#discussioncomment-9602092

from app.models.user_model import User, UserPublic
from app.models.post_model import Post, PostPublic

PostPublic.model_rebuild()
UserPublic.model_rebuild()