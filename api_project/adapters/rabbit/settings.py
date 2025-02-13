from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    RABBIT_USER: str = 'guest'
    RABBIT_PASS: str = 'guest'
    RABBIT_HOST: str = 'localhost'
    RABBIT_PROTOCOL: str = 'amqp'
    RABBIT_BASE_QUEUE: str = 'base_queue'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='allow',
    )

    @property
    def RABBIT_URL(self):
        url = "{protocol}://{user}:{password}@{host}/"

        return url.format(
            protocol=self.RABBIT_PROTOCOL,
            user=self.RABBIT_USER,
            password=self.RABBIT_PASS,
            host=self.RABBIT_HOST,
        )
