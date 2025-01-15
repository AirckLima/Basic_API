from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, BigInteger, Enum, Interval
from sqlalchemy.orm import relationship, Mapped
from app.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)

    username = Column(String, index=True)
    age = Column(Integer)
    email = Column(Integer, index=True)
    password = Column(String)


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), index=True)

    user: Mapped["User"] = relationship()
    posts: Mapped[list["Post"]] = relationship(back_populates="profile")


class Post(Base):
    __tablename__ = "post"

    id = Column(primary_key=True, index=True)
    profile_id = Column(ForeignKey("profile.id"), index=True)

    conent = Column(String)

    profile: Mapped["Profile"] = relationship(back_populates="posts")