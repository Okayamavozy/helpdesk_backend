from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.tasks import TaskEntity, TaskStatuses, TaskCategories

from backend.interfaces.tasks import ITaskRepository

class SqlAlchemyTaskRepository(ITaskRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all(self) -> list[TaskEntity]:
        result = select(TaskEntity).order_by(TaskEntity.id)
        result = await self.session.scalars(result)
        return list(result.all())

    async def get_by_id(self, task_id: int) -> TaskEntity | None:
        return await self.session.get(TaskEntity, task_id)

    async def change_status(self, task_id: int, new_status: TaskStatuses) -> TaskEntity | None:
        task = await self.get_by_id(task_id)
        if task is None:
            return None
        task.status = new_status
        await self.session.flush()
        return task

    async def create(self, title: str, description: str, category: TaskCategories, author_id: int) -> TaskEntity:
        task = TaskEntity(
            title = title,
            description = description,
            status = TaskStatuses.TODO,
            category = category,
            author_id = author_id
        )
        self.session.add(task)
        await self.session.flush()
        return task

    async def delete(self, task_id: int) -> bool:
        task = await self.get_by_id(task_id)
        if task is None:
            return False
        await self.session.delete(task)
        await self.session.flush()
        return True