from contextlib import asynccontextmanager
from fastapi import FastAPI

import uvicorn

from backend.config.database import Base, engine

from backend.models.tasks import TaskEntity
from backend.models.users import UserEntity

from backend.routers.users import router as users_router
from backend.routers.tasks import router as tasks_router

from backend.middlewares.middleware import ExceptionHandlerMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(title="HelpDeskAPI", lifespan=lifespan)

app.include_router(users_router)
app.include_router(tasks_router)

app.add_middleware(ExceptionHandlerMiddleware)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)