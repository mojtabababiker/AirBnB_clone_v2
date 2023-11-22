#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Intger, Float, ForeignKey
from sqlalchemy.orm import relationship, aliased
import os


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeginKey("cities.id"))
    user_id = Column(String(60), nullable=False, ForeginKey("users.id"))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", bakref="place",
                               cascade="all, delete-orphan")
    else:
        from models import storage
        reviews = [rev for rev in storage.all("Review").values()
                   if rev.place_id == self.id]

    # amenity_ids = []


aliased_palce = aliased(Place, "place")
