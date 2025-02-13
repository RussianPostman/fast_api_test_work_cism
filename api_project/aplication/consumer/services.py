import json
import logging
from dataclasses import dataclass

from aio_pika.abc import AbstractIncomingMessage

from api_project.domain.tasks.emulator import Emulator
from api_project.domain.tasks.entities import TaskStatusEnum
from api_project.aplication.tasks.interfaces import TaskDatabaseInterface

logger = logging.getLogger("consumer")


@dataclass
class ConsumerService:
    database: TaskDatabaseInterface

    async def _important_work(
        self,
        task_id: int,
    ) -> int:

        await self.database.update_task_status(
            task_id=task_id,
            new_status=TaskStatusEnum.IN_PROGRESS,
        )
        logger.info(
            f"Статус задачи {task_id} обновлён до {TaskStatusEnum.IN_PROGRESS}."
        )

        important_data = await Emulator.emulate()
        logger.info(f"Эмулятор отработал с результатом {important_data}.")

        if important_data:
            await self.database.update_task_status(
                task_id=task_id,
                new_status=TaskStatusEnum.COMPLETED,
            )
            logger.info(
                f"Статус задачи {task_id} "
                f"обновлён до {TaskStatusEnum.IN_PROGRESS}."
            )
        else:
            await self.database.update_task_status(
                task_id=task_id,
                new_status=TaskStatusEnum.FAILED,
            )
            logger.info(
                f"Статус задачи {task_id} "
                f"обновлён до {TaskStatusEnum.FAILED}."
            )

        return important_data

    async def on_message(self, message: AbstractIncomingMessage) -> None:
        async with message.process():
            logger.info("Получено сообщение.")

            body = message.body.decode("utf-8")
            data = json.loads(body)

            work_status = await self._important_work(data['task_id'])

            if work_status:
                logger.info(f"Задача {data['task_id']} завершина.")

            else:
                logger.error(f"Задача {data['task_id']} провалена.")
