#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

rabbitmq_ready() {
    python << END
import sys
import aio_pika

async def check_rabbitmq():
    try:
        connection = await aio_pika.connect_robust("amqp://${RABBIT_USER}:${RABBIT_PASS}@${RABBIT_HOST}/")
        await connection.close()
        return True
    except Exception:
        return False

import asyncio
if not asyncio.run(check_rabbitmq()):
    sys.exit(-1)
sys.exit(0)
END
}

until rabbitmq_ready; do
  >&2 echo 'Waiting for RabbitMQ to become available...'
  sleep 1
done
>&2 echo 'RabbitMQ is available'

python -m api_project.composites.consumer
