from datetime import datetime

from pydantic import BaseModel

from api_project.domain.tasks.entities import TaskStatusEnum


class CreateTaskReqest(BaseModel):
    name: str


class CreateTaskResponse(BaseModel):
    task_id: int


class Task(BaseModel):
    id: int
    name: str
    created_at: datetime
    status: TaskStatusEnum

    @classmethod
    def init(cls, task: dict):
        return cls(
            id=task.get('id'),
            name=task.get('name'),
            created_at=task.get('created_at'),
            status=task.get('status'),
        )
