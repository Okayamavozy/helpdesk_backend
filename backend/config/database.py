import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")

if db_url is None:
    raise RuntimeError("Переменная окружения не задана")

engine = create_engine(db_url)
session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass