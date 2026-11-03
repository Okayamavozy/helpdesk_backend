from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from backend.config.database import Base, engine

from backend.models.Tasks import TasksEntity
from backend.models.Users import UserEntity

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    print("Таблицы успешно созданы")
    yield

app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)