from fastapi import APIRouter, HTTPException, Depends, Body
from sqlalchemy.orm import Session
from database import SessionLocal
from models.models import Projects as ProjectModel
import uuid
from typing import Optional, List
from uuid import UUID

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/project", response_model=dict)
def create_project(
    title: str = Body(...), 
    description: Optional[str] = Body(None), 
    completed: Optional[bool] = Body(False), 
    attribution: Optional[str] = Body(None), 
    db: Session = Depends(get_db)
):
    db_project = ProjectModel(
        id=str(uuid.uuid4()),
        title=title,
        description=description,
        completed=completed,
        attribution=attribution
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return {
        "id": str(db_project.id),
        "title": db_project.title,
        "description": db_project.description,
        "completed": db_project.completed,
        "attribution": db_project.attribution
    }

@router.get("/projects/{project_id}", response_model=dict)
def read_project(project_id: UUID, db: Session = Depends(get_db)):
    project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {
        "id": str(project.id),
        "title": project.title,
        "description": project.description,
        "completed": project.completed,
        "attribution": project.attribution
    }

@router.get("/projects", response_model=List[dict])
def get_projects_all(db: Session = Depends(get_db)):
    projects = db.query(ProjectModel).all()
    return [
        {
            "id": str(project.id),
            "title": project.title,
            "description": project.description,
            "completed": project.completed,
            "attribution": project.attribution
        }
        for project in projects
    ]

@router.get("/nbrProjects", response_model=dict)
def get_number_of_projects(db: Session = Depends(get_db)):
    project_count = db.query(ProjectModel).count()
    return {"number_of_projects": project_count}
