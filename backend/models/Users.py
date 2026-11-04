from sqlalchemy.orm import Mapped, mapped_column

from backend.config.database import Base

class UserEntity(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    department: Mapped[str] 
