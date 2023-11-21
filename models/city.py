from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
