from api_project.adapters.db import Settings as DBSettings
from api_project.adapters.rabbit import Settings as RabbitSettings
from api_project.adapters.db.repositories.tasks import TaskRepository
from api_project.adapters.rabbit.publisher import RabbitRepo
from api_project.aplication.tasks.services import TaskService

db_settings = DBSettings()
rabbit_settings = RabbitSettings()

task_repository = TaskRepository(db_settings.DATABASE_URL)
rabbit_repo = RabbitRepo(rabbit_settings.RABBIT_URL)

task_service = TaskService(database=task_repository, rabbit=rabbit_repo)


def get_task_service() -> TaskService:
    return task_service
