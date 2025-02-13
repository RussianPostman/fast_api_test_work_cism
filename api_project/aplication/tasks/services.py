from dataclasses import dataclass
from datetime import datetime

from api_project.domain.tasks.entities import TaskStatusEnum
from api_project.aplication.tasks.interfaces import TaskDatabaseInterface, TaskRabbitInterface


@dataclass
class TaskService:
    database: TaskDatabaseInterface
    rabbit: TaskRabbitInterface

    async def add_task(
        self,
        name: str,
    ) -> int:
        task_id = await self.database.create_task(name)
        await self.rabbit.create_message(task_id)

        return task_id

    async def get_task(
        self,
        task_id: int,
    ) -> dict[str, str | datetime]:
        return await self.database.get_task(task_id=task_id)

    async def get_task_list(
        self,
        status: TaskStatusEnum = None
    ) -> list[dict[str, str | datetime]]:

        return await self.database.get_tasks(status)

    async def update_task_status(
        self,
        task_id: int,
        status: TaskStatusEnum,
    ) -> dict[str, str | datetime]:
        return await self.database.update_task_status(
            task_id=task_id,
            new_status=status,
        )


