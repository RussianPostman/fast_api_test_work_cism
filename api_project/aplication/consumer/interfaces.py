from abc import ABC, abstractmethod

from api_project.domain.tasks.entities import TaskStatusEnum


class ConsumerInterface(ABC):

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
