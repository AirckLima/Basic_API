# from sqlmodel import SQLModel, Field, Relationship
# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     # from app.models.exemple_model import Profile, ExemplePublic


# class PostBase(SQLModel):
#     content: str


# class Post(PostBase, table=True):
#     id: int = Field(primary_key=True, index=True)
#     profile_id: int = Field(foreign_key="profile.id", index=True)

#     profile: "Profile" = Relationship(back_populates="posts")
    

# class PostCreate(PostBase):
#     profile_id: int
    


# class PostPublic(PostBase):
#     id: int

#     profile: "ProfilePublic"


# class PostUpdate(PostBase):
#     pass


# # https://github.com/fastapi/sqlmodel/discussions/757#discussioncomment-9602092

# from app.models.exemple_model import Profile, ProfilePublic

# ProfilePublic.model_rebuild()