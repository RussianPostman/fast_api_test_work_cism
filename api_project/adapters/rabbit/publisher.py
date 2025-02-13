import json
import aio_pika

from api_project.aplication.tasks.interfaces import TaskRabbitInterface


class RabbitRepo(TaskRabbitInterface):
    url: str
    base_queue: str

    def __init__(self, url, base_queue: str = 'base_queue') -> None:
        self.url = url
        self.base_queue = base_queue

    async def create_message(
        self,
        task_id: int
    ) -> None:
        json_data = json.dumps({'task_id': task_id}).encode("utf-8")

        message = aio_pika.Message(
            body=json_data,
            content_type="application/json",
        )

        connection = await aio_pika.connect_robust(self.url)

        async with connection:

            channel = await connection.channel()
            queue = await channel.declare_queue(self.base_queue, durable=True)

            await channel.default_exchange.publish(
                message,
                routing_key=queue.name,
            )
