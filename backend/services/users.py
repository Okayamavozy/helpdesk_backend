from backend.repositories.users import SqlAlchemyUserRepository
from backend.schemas.users import CreateUserSchema
from backend.models.users import UserEntity

from backend.validations.errors import NotFoundError

class UserService:
    def __init__(self, user_repository: SqlAlchemyUserRepository):
        self.repository = user_repository

    def create_user(self, schema: CreateUserSchema) -> UserEntity:
        return self.repository.create(schema.username, schema.department)

    def get_all_users(self) -> list[UserEntity]: 
        users = self.repository.get_all()
        if not users:
            raise NotFoundError("Пользователей не существует")
        return users

    def get_by_user_id(self, user_id: int) -> UserEntity: 
        user = self.repository.get_by_id(user_id)
        if not user:
            raise NotFoundError("Пользователь с таким ID не найден")
        return user
