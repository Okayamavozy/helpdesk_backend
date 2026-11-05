from fastapi import APIRouter, status
from backend.schemas.users import CreateUserSchema, UserResponseSchema
from backend.dependencies.deps import UserServiceDep

router = APIRouter(prefix="/api/v1/users", tags=["Users"])


@router.post("", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
def create_user(schema: CreateUserSchema, service: UserServiceDep):
    """Создать нового пользователя"""
    return service.create_user(schema)

@router.get("", response_model=list[UserResponseSchema])
def get_all_users(service: UserServiceDep):
    """Получить список пользователей"""
    return service.get_all_users()

@router.get("/{user_id}", response_model=UserResponseSchema)
def get_user_by_id(user_id: int, service: UserServiceDep):
    """Получить пользователя по его ID"""
    return service.get_user_by_id(user_id)

@router.delete("/{user_id}", response_model=dict[str, str])
def delete_user(user_id: int, service: UserServiceDep):
    """Удалить пользователя"""
    return service.delete_user(user_id)