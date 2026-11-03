from pydantic import BaseModel, Field

from backend.config.schema_config import base_config
from backend.models.tasks import TaskCategories, TaskStatuses

class CreateTaskSchema(BaseModel):
    title: str = Field(min_length=5, max_length=25)
    description: str = Field(max_length=512)
    category: TaskCategories
    author_id: int

    model_config = base_config


class ChangeStatusSchema(BaseModel):
    task_id: int = Field(gt=0)
    status: TaskStatuses

    model_config = base_config