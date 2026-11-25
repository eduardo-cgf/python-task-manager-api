from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from . import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="A simple API to manage tasks.",
    version="0.1.0",
)

@app.get("/")
def home():
    return {
        "message": "Welcome to the Task Manager API!"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.post("/tasks", response_model=schemas.TaskResponse, status_code=201)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):

    new_task = models.Task(
        title=task.title,
        description=task.description,
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task