from fastapi import Depends
from sqlalchemy.orm import Session

from backend.config.database import get_session
from backend.services.users import UserService
from backend.repositories.users import SqlAlchemyUserRepository


def get_user_service(session: Session = Depends(get_session)) -> UserService:
    return UserService(SqlAlchemyUserRepository(session))