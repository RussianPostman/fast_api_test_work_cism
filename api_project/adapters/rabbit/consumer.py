import asyncio
import logging

from aio_pika import connect

from api_project.adapters.rabbit import Settings as RabbitSettings
from api_project.aplication.consumer.services import ConsumerService


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("consumer")


async def main_consumer(
    settings: RabbitSettings,
    service: ConsumerService,
) -> None:
    print(settings.RABBIT_URL)
    connection = await connect(settings.RABBIT_URL)
    logger.info("Подключение к RabbitMQ успешно установлено.")

    async with connection:
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)

        queue = await channel.declare_queue(
            settings.RABBIT_BASE_QUEUE,
            durable=True,
        )

        await queue.consume(service.on_message)

        await asyncio.Future()
