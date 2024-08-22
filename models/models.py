from sqlalchemy import Column, CHAR, Integer, String, Boolean, Text
from database import Base
import uuid

class Projects(Base):
    __tablename__ = "projects"
    
    id = Column(CHAR(36), primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    completed = Column(Boolean, default=False)
    attribution = Column(String)
