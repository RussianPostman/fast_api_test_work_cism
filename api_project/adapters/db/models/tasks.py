from datetime import datetime

from sqlalchemy import Enum, func
from sqlalchemy.orm import Mapped, mapped_column

from api_project.domain.tasks.entities import TaskStatusEnum
from . import BaseModel


class Task(BaseModel):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    status: Mapped[TaskStatusEnum] = mapped_column(Enum(TaskStatusEnum))

    def todict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'status': self.status,
        }
