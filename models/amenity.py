#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

storage_type = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    name = ""
