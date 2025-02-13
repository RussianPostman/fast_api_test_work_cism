from abc import ABC, abstractmethod

from api_project.domain.tasks.entities import TaskStatusEnum


class TaskDatabaseInterface(ABC):

    @abstractmethod
    async def create_task(
        self,
        name: str = None,
    ):
        """
        Создаёт новую задачу
        """
        ...

    @abstractmethod
    async def update_task_status(
        self,
        task_id: int,
        new_status: TaskStatusEnum,
    ):
        """
        Обновляет статус задачи по её ID.
        """
        ...

    @abstractmethod
    async def get_task(
        self,
        task_id: int,
    ):
        """
        Возвращает задачу по её ID.
        """
        ...

    @abstractmethod
    async def get_tasks(
        self,
        status: TaskStatusEnum = None,
    ):
        ...


class TaskRabbitInterface(ABC):

    @abstractmethod
    async def create_message(self, task_id: int) -> None:
        ...
