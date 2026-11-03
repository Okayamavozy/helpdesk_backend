from pydantic import BaseModel, Field, ConfigDict

from backend.config.schema_config import base_config
from backend.models.tasks import TaskCategories, TaskStatuses

class CreateTaskSchema(BaseModel):
    title: str = Field(min_length=5, max_length=25)
    description: str = Field(max_length=512)
    category: TaskCategories
    author_id: int

    model_config = base_config


class ChangeTaskStatusSchema(BaseModel):
    task_id: int = Field(gt=0)
    status: TaskStatuses

    model_config = base_config


class TaskResponseSchema(BaseModel):
    id: int
    title: str
    status: TaskStatuses
    category: TaskCategories
    description: str
    author_id: int
    executor_id: int | None = None

    model_config = base_config