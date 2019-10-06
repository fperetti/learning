# flask_sqlalchemy/models.py
from db import Base
from sqlalchemy import *
from sqlalchemy.orm import (relationship, backref)

class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)