from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # Relationship with City
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
