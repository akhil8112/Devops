from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Task API")


class Task(BaseModel):
    title: str
    completed: bool = False


tasks = [
    {
        "id": 1,
        "title": "Learn CI/CD",
        "completed": False
    }
]


@app.get("/")
def home():
    return {"message": "Task API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": task.completed
    }
    new_task2= {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)
    tasks.append(new_task2)

    return new_task