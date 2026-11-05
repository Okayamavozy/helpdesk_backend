from backend.interfaces.tasks import ITaskRepository
from backend.schemas.tasks import CreateTaskSchema
from backend.models.tasks import TaskEntity, TaskStatuses, TaskCategories

from backend.validations.errors import NotFoundError

class TaskService:
    def __init__(self, task_repository: ITaskRepository):
        self.repository = task_repository

    async def create_task(self, schema: CreateTaskSchema) -> TaskEntity:
        return await self.repository.create(schema.title, schema.description, schema.category, schema.author_id) 

    async def get_all_tasks(self) -> list[TaskEntity]:
        tasks = await self.repository.get_all()
        return tasks

    async def get_task_by_id(self, task_id: int) -> TaskEntity:
        task = await self.repository.get_by_id(task_id) 
        if not task:
            raise NotFoundError(f"Задача {task_id} не найдена")
        return task

    async def change_status(self, task_id: int, new_status: TaskStatuses) -> TaskEntity:
        task = await self.repository.change_status(task_id, new_status)
        if task is None: 
            raise NotFoundError(f"Задача с {task_id} не найдена")
        return task

    async def return_statuses(self) -> dict[str, str]:
        return { status.name: status.value for status in TaskStatuses }

    async def return_categories(self) -> dict[str, str]:
        return { category.name: category.value for category in TaskCategories}

    async def delete_task(self, task_id: int) -> dict[str, str]:
        if not await self.repository.delete(task_id):
            raise NotFoundError(f"Задача {task_id} не найдена")
        return {"message": f"Задача {task_id} удалена"}
        
