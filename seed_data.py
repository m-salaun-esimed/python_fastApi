from sqlalchemy.orm import Session
from database import SessionLocal
from models.models import Projects
import uuid

def delete_all_projects(db: Session):
    db.query(Projects).delete()
    db.commit()

def seed_projects(db: Session):
    projects = [
        {
            "title": "ORIFICE DE COQUE",
            "description": "This is the first project.",
            "completed": False,
            "attribution": "Team A"
        },
        {
            "title": "FLOPHIB",
            "description": "This is the second project.",
            "completed": True,
            "attribution": "Team B"
        },
        {
            "title": "RADIOWAR",
            "description": "This is the third project.",
            "completed": False,
            "attribution": "Team C"
        },
        {
            "title": "PLONGEUR",
            "description": "This is the fourth project.",
            "completed": True,
            "attribution": "Team D"
        },
    ]

    for project_data in projects:
        project = Projects(
            id=str(uuid.uuid4()),
            title=project_data["title"],
            description=project_data["description"],
            completed=project_data["completed"],
            attribution=project_data["attribution"]
        )
        db.add(project)

    db.commit()  # Enregistrer les nouveaux projets

def main():
    db = SessionLocal()
    try:
        delete_all_projects(db)
        seed_projects(db)
    finally:
        db.close()

if __name__ == "__main__":
    main()
