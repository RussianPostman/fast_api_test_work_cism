from datetime import datetime

from sqlalchemy import update, select

from api_project.adapters.db.models import Task
from api_project.adapters.db.repositories import BaseRepository
from api_project.aplication.consumer.interfaces import ConsumerInterface
from api_project.aplication.tasks.interfaces import TaskDatabaseInterface
from api_project.domain.tasks.entities import TaskStatusEnum


class TaskRepository(BaseRepository, TaskDatabaseInterface, ConsumerInterface):

    async def create_task(
        self,
        name: str = None,
    ) -> int:
        """
        Создаёт новую задачу.
        """
        async with self.get_session_maker()() as session:
            async with session.begin():
                new_task = Task(name=name, status=TaskStatusEnum.NEW)
                session.add(new_task)
                await session.flush()
                await session.refresh(new_task)
                return new_task.id

    async def update_task_status(
        self,
        task_id: int,
        new_status: TaskStatusEnum,
    ) -> dict[str, str | datetime | int] | None:
        """
        Обновляет статус задачи по её ID.
        """
        async with self.get_session_maker()() as session:
            async with session.begin():

                query = select(Task).where(Task.id == task_id)
                result = await session.execute(query)
                task = result.scalars().first()

                if task:
                    task.status = new_status
                    await session.commit()
                    return task.todict()

                return None

    async def get_task(
        self,
        task_id: int,
    ) -> dict | None:
        """
        Возвращает задачу по её ID.
        """
        async with self.get_session_maker()() as session:
            async with session.begin():
                query = await session.execute(
                    select(Task).where(Task.id == task_id)
                )

                if result := query.scalars().first():
                    return result.todict()

                return None

    async def get_tasks(
        self,
        status: TaskStatusEnum = None,
    ) -> list[dict[str, str | datetime]]:
        """
        Возвращает список задач.
        """
        async with self.get_session_maker()() as session:
            async with session.begin():
                qery = select(Task)

                if status:
                    qery = qery.where(Task.status == status)

                result = await session.execute(qery)
                return [task.todict() for task in result.scalars().all()]
