from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.models.users import UserEntity

class SqlAlchemyUserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self) -> list[UserEntity] | None:
        result = select(UserEntity).order_by(UserEntity.id)
        return list(self.session.scalars(result).all())

    def get_by_id(self, user_id: int) -> UserEntity | None:
        result = select(UserEntity).where(UserEntity.id == user_id)
        return self.session.scalars(result).one_or_none()

    def create(self, user: UserEntity) -> UserEntity:
        self.session.add(user)
        self.session.flush()
        return user