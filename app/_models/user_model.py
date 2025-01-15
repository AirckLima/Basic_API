from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import TYPE_CHECKING, Union, Optional, List

if TYPE_CHECKING:
    pass


class UserBase(SQLModel):
    username: str = Field(index=True)
    age: int
    

class UserExtend(UserBase):
    email: str = Field(index=True)


class User(UserExtend, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str


class UserCreate(UserExtend):
    password: str


class UserPublic(UserBase):
    id: int


class UserUpdate(UserBase):
    pass