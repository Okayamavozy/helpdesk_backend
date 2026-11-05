import os
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")

if db_url is None:
    raise RuntimeError("Переменная окружения не задана")

engine = create_async_engine(db_url)
sessionLocal = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass


async def get_session():
    async with sessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise