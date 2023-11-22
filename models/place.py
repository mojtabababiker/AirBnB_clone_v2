#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import Base, BaseModel
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, aliased
import os


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
    else:
        @property
        def reviews(self):
            """ Return self.reviews """
            from models import storage
            reviews = [rev for rev in storage.all(Review).values()
                       if rev.place_id == self.id]
            return reviews

    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ Initiate the instance with some default values and call the
        super init to complete the initiate
        """
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        super().__init__(*args, **kwargs)


aliased_place = aliased(Place, "place")
