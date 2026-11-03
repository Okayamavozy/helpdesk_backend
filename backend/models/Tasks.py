from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum

from backend.config.database import Base


class TaskStatuses(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class TaskCategories(str, Enum):
    INTERNET = "internet"
    PC = "pc"
    MAIL = "mail"
    OTHER = "other"


class TasksEntity(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(25))
    status: Mapped[TaskStatuses]
    category: Mapped[TaskCategories]
    description: Mapped[str] = mapped_column(String(512))
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    executor_id: Mapped[int | None ] = mapped_column(ForeignKey("users.id"))