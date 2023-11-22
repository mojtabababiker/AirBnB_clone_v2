#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """ Initiate the instance with some default values and call the
        super init to complete the initiate
        """
        super().__init__(*args, **kwargs)
