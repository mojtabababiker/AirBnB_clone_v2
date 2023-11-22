from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, aliased
import os


class State(BaseModel, Base):
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # in databases systems
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        # Relationship with City
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    # in file_storage systems
    else:
        cities = [city for city in storage.all("City").values()
                  if city.state_id == self.id]


aliased_state = aliased(State, name='state')
