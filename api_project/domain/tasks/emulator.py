import random
import asyncio


class Emulator:

    @staticmethod
    async def emulate() -> bool:
        await asyncio.sleep(random.randrange(2, 8))

        return random.random() < 0.8
