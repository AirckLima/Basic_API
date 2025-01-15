from pydantic import BaseModel, ConfigDict, Field, computed_field


class OrmBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class UserBase(OrmBaseModel):
    username: str
    age: int
    

class UserExtend(UserBase):
    email: str


class User(UserExtend):
    id: int
    password: str


class UserCreate(UserExtend):
    password: str


class UserResponse(UserBase):
    id: int


class UserUpdate(UserBase):
    pass


class ProfileBase(OrmBaseModel):
    nickname: str
    avatar: str | None = Field(default=None)
    bio: str | None = Field(default=None)


class Profile(ProfileBase):
    id: int 
    user_id: int 

    user: "UserResponse" 
    posts: list["PostResponse"]


class ProfileCreate(ProfileBase):
    user_id: int


class ProfileResponse(ProfileBase):
    id: int



class ProfileUpdate(ProfileBase):
    pass


class PostBase(OrmBaseModel):
    content: str


class Post(PostBase):
    id: int
    profile_id: int

    profile: "ProfileResponse"
    

class PostCreate(PostBase):
    profile_id: int
    

class PostResponse(PostBase):
    id: int



class PostUpdate(PostBase):
    pass