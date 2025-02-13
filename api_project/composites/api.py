from fastapi import FastAPI

from api_project.adapters.api.tasks.router import task_router

app = FastAPI()

app.include_router(task_router)


@app.get("/")
def test_end():
    return {"message": "Hello World"}
