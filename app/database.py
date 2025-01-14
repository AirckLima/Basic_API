from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv
import os


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

connect_args = {"check_same_thread": False}


if DATABASE_URL:
    engine = create_engine(
        DATABASE_URL, 
        connect_args=connect_args
    )


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_db_session():
    with Session(engine) as session:
        yield session
