from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class OrmBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    username: str | None = Field(default=None)


class UserBaseSchema(OrmBaseModel):
    username: str
    age: int
    email: str
    

class UserSchema(UserBaseSchema):
    id: int


class UserDBSchema(UserSchema):
    hashed_password: str


class UserCreateSchema(UserSchema):
    hashed_password: str
    


class UserReferenceSchema(UserBaseSchema):
    id: int


class UserUpdateSchema(UserBaseSchema):
    pass



class ProfileBaseSchema(OrmBaseModel):
    nickname: str
    avatar: str | None = Field(default=None)
    bio: str | None = Field(default=None)


class ProfileSchema(ProfileBaseSchema):
    id: int 
    user_id: int 

    user: Optional["UserReferenceSchema"] = None
    posts: Optional[list["PostReferenceSchema"]] = None


class ProfileCreateSchema(ProfileBaseSchema):
    user_id: int


class ProfileReferenceSchema(ProfileBaseSchema):
    id: int


class ProfileUpdateSchema(ProfileBaseSchema):
    pass



class PostBaseSchema(OrmBaseModel):
    content: str


class PostSchema(PostBaseSchema):
    id: int
    profile_id: int

    profile: Optional["ProfileReferenceSchema"] = None
    

class PostCreateSchema(PostBaseSchema):
    profile_id: int
    

class PostReferenceSchema(PostBaseSchema):
    id: int



class PostUpdateSchema(PostBaseSchema):
    pass