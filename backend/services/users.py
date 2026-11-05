from backend.repositories.users import SqlAlchemyUserRepository
from backend.interfaces.users import IUserRepository
from backend.schemas.users import CreateUserSchema
from backend.models.users import UserEntity

from backend.validations.errors import NotFoundError

class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.repository = user_repository

    async def create_user(self, schema: CreateUserSchema) -> UserEntity:
        return await self.repository.create(schema.username, schema.department)

    async def get_all_users(self) -> list[UserEntity]:
        return await self.repository.get_all()
    
    async def get_user_by_id(self, user_id: int) -> UserEntity: 
        user = await self.repository.get_by_id(user_id)
        if not user:
            raise NotFoundError(f"Пользователь с ID {user_id} не найден")
        return user

    async def delete_user(self, user_id: int) -> dict[str, str]:
        if not await self.repository.delete(user_id):
            raise NotFoundError(f"Пользователь {user_id} не найден")
        return {"message": "Пользователь удален"}
