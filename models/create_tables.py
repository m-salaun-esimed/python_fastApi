from database import engine, Base
from models import Projects

Base.metadata.create_all(bind=engine)
