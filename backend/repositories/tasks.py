from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.models.tasks import TaskEntity, TaskStatuses, TaskCategories

class SqlAlchemyTaskRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self) -> list[TaskEntity]:
        result = select(TaskEntity).order_by(TaskEntity.id)
        return list(self.session.scalars(result).all())

    def get_by_id(self, task_id: int) -> TaskEntity | None:
        result = select(TaskEntity).where(TaskEntity.id == task_id)
        return self.session.scalars(result).one_or_none()

    def change_status(self, task_id: int, new_status: TaskStatuses) -> TaskEntity | None:
        task = self.get_by_id(task_id)
        if not task:
            return None
        task.status = new_status
        self.session.flush()
        return task

    def get_statuses(self) -> list[TaskStatuses]:
        return list(TaskStatuses)

    def create(self, title: str, description: str, category: TaskCategories, author_id: int) -> TaskEntity:
        task = TaskEntity(
            title = title,
            description = description,
            status = TaskStatuses.TODO,
            category = category,
            author_id = author_id
        )
        self.session.add(task)
        self.session.flush()
        return task