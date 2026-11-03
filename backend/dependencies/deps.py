from fastapi import Depends
from sqlalchemy.orm import Session

from backend.config.database import get_session

from backend.services.users import UserService
from backend.services.tasks import TaskService

from backend.repositories.users import SqlAlchemyUserRepository
from backend.repositories.tasks import SqlAlchemyTaskRepository


def get_user_service(session: Session = Depends(get_session)) -> UserService:
    return UserService(SqlAlchemyUserRepository(session))

def get_task_service(session: Session = Depends(get_session)) -> TaskService:
    return TaskService(SqlAlchemyTaskRepository(session))