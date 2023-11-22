#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)


    def __init__(self, *args, **kwargs):
        """ Initiate the instance with some default values and call the
        super init to complete the initiate
        """
        self.text = ""
        self.place_id = ""
        self.user_id = ""
        super().__init__(*args, **kwargs)

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    user = relationship("User", back_populates="reviews", foreign_keys=[user_id])
else:
    @property
    def user(self):
        """ Getter attribute for user when using FileStorage """
        from models import storage
        return storage.get("User", self.user_id)

# For Place
if os.getenv("HBNB_TYPE_STORAGE") == "db":
    place = relationship("Place", back_populates="reviews", foreign_keys=[place_id])
else:
    @property
    def place(self):
        """ Getter attribute for place when using FileStorage """
        from models import storage
        return storage.get("Place", self.place_id)
