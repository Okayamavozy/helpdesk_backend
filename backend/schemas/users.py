from pydantic import BaseModel, Field, ConfigDict
from backend.config.schema_config import base_config

class CreateUserSchema(BaseModel):
    username: str = Field(min_length=1)
    department: str = Field(min_length=1)

    model_config = base_config


class UserResponseSchema(BaseModel):
    id: int
    username: str
    department: str

    model_config = base_config