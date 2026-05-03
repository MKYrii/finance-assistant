from sqlalchemy import MetaData
from sqlmodel import SQLModel, Session, create_engine
from app.core.config import DB_URL

engine = create_engine(DB_URL, echo=True)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


sqlite_naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

SQLModel.metadata = MetaData(naming_convention=sqlite_naming_convention)