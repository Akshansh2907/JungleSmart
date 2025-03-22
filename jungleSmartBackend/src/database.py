from sqlmodel import create_engine, Session
from fastapi import Depends
from src.models import SQLModel
from typing import Annotated

from src.config import Config

engine = create_engine(
    url=Config.DATABASE_URL,
    echo=True,
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
