import asyncio

from aiormq import AMQPConnectionError

from api_project.adapters.db import Settings as DBSettings
from api_project.adapters.rabbit import Settings as RabbitSettings
from api_project.adapters.db.repositories.tasks import TaskRepository
from api_project.adapters.rabbit.consumer import main_consumer
from api_project.aplication.consumer.services import ConsumerService


db_settings = DBSettings()
rabbit_settings = RabbitSettings()

task_repository = TaskRepository(db_settings.DATABASE_URL)
consumer_service = ConsumerService(task_repository)


if __name__ == '__main__':
    asyncio.run(main_consumer(rabbit_settings, consumer_service))
