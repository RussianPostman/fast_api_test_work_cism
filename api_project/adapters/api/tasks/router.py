from fastapi import APIRouter, Body, Depends, HTTPException

from api_project.adapters.api.tasks.schemes import CreateTaskReqest, CreateTaskResponse, Task
from api_project.aplication.app import get_task_service
from api_project.aplication.tasks.services import TaskService
from api_project.domain.tasks.entities import TaskStatusEnum

task_router = APIRouter(
   prefix="/tasks",
   tags=["Фоновые задачи"],
)


@task_router.post("/")
async def create_task(
    request: CreateTaskReqest = Body(),
    task_service: TaskService = Depends(get_task_service)
) -> CreateTaskResponse:

    return CreateTaskResponse(
        task_id = await task_service.add_task(name=request.name)
    )

@task_router.get("/")
async def list_tasks(
    status: TaskStatusEnum = None,
    task_service: TaskService = Depends(get_task_service),
):
    return [
        Task.init(task) for task in
        await task_service.get_task_list(status=status)
    ]


@task_router.get(
    "/{task_id}",
    response_model=Task
)
async def get_task(
    task_id: int,
    task_service: TaskService = Depends(get_task_service),
) -> Task:
    task_response = await task_service.get_task(
        task_id=task_id,
    )

    if task_response:
        return Task.init(task_response)

    else:
        raise HTTPException(
            status_code=400,
            detail='Несуществующий task_id',
        )
