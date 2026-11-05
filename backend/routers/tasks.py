from fastapi import APIRouter, status
from backend.models.tasks import TaskStatuses
from backend.schemas.tasks import TaskResponseSchema, ChangeTaskStatusSchema, CreateTaskSchema
from backend.dependencies.deps import TaskServiceDep

router = APIRouter(prefix="/api/v1/tasks", tags=["Tasks"])

@router.post("", response_model=CreateTaskSchema, status_code=status.HTTP_201_CREATED)
async def create_task(schema: CreateTaskSchema, service: TaskServiceDep):
    """Создать новую задачу"""
    return await service.create_task(schema)

@router.get("", response_model=list[TaskResponseSchema])
async def get_all_tasks(service: TaskServiceDep):
    """Получить список задач"""
    return await service.get_all_tasks()

@router.get("/statuses", response_model=dict[str, str])
async def get_statuses(service: TaskServiceDep):
    """Получить возможные статусы задачи"""
    return await service.return_statuses()

@router.get("/categories", response_model=dict[str, str])
async def get_categories(service: TaskServiceDep):
    """Получить возможные категории задачи"""
    return await service.return_categories()

@router.patch("/{task_id}/status", response_model=ChangeTaskStatusSchema)
async def change_status(task_id: int, new_status: TaskStatuses, service: TaskServiceDep):
    """Изменить статус задачи"""
    return await service.change_status(task_id, new_status)

@router.get("/{task_id}", response_model=TaskResponseSchema)
async def get_task_by_id(task_id: int, service: TaskServiceDep):
    """Получить задачу по ее ID"""
    return await service.get_task_by_id(task_id)

@router.delete("/{task_id}", response_model=dict[str, str])
async def delete_task(task_id: int, service: TaskServiceDep):
    """Удалить задачу"""
    return await service.delete_task(task_id)