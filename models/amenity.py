#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Table, Column, String


class Amenity(BaseModel, Base):
    __tablename = "amenities"
    name = Column(String(128), nullable=False)
