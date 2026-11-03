from typing import Protocol
from backend.models.users import UserEntity


class IUserRepository(Protocol):
    def get_by_id(self, user_id: int) -> UserEntity | None: ...
    def create(self, user: UserEntity) -> UserEntity: ...