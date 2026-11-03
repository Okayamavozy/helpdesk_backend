from backend.repositories.tasks import SqlAlchemyTaskRepository
from backend.schemas.tasks import CreateTaskSchema
from backend.models.tasks import TaskEntity, TaskStatuses

from backend.validations.errors import NotFoundError

class TaskService:
    def __init__(self, task_repository: SqlAlchemyTaskRepository):
        self.repository = task_repository

    def create_task(self, schema: CreateTaskSchema) -> TaskEntity:
        return self.repository.create(schema.title, schema.description, schema.category, schema.author_id) 

    def get_all_tasks(self) -> list[TaskEntity]:
        tasks = self.repository.get_all()
        if not tasks:
            raise NotFoundError("Ни одна задача не создана")   
        return tasks

    def get_task_by_id(self, task_id: int) -> TaskEntity:
        task = self.repository.get_by_id(task_id) 
        if not task:
            raise NotFoundError(f"Задача {task_id} не найдена")
        return task

    def change_status(self, task_id: int, new_status: TaskStatuses) -> TaskEntity:
        task = self.repository.change_status(task_id, new_status)
        if task is None: 
            raise NotFoundError(f"Задача с {task_id} не найдена")
        return task

    def return_statuses(self) -> list[TaskStatuses]:
        return list(TaskStatuses)
