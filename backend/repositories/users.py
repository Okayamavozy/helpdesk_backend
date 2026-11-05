from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.interfaces.users import IUserRepository

from backend.models.users import UserEntity

class SqlAlchemyUserRepository(IUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all(self) -> list[UserEntity]:
        stmt = select(UserEntity).order_by(UserEntity.id)
        result = await self.session.scalars(stmt)
        return list(result.all())
        

    async def get_by_id(self, user_id: int) -> UserEntity | None:
        return await self.session.get(UserEntity, user_id)

    async def create(self, username: str, department: str) -> UserEntity:
        user = UserEntity(
            username = username,
            department = department
        )
        self.session.add(user)
        await self.session.flush()
        return user

    async def delete(self, user_id: int) -> bool:
        user = await self.get_by_id(user_id)
        if user is None:
            return False
        await self.session.delete(user)
        await self.session.flush()
        return True