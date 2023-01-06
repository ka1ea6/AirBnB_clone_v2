#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

storage_type = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    if storage_type == 'db':
        from models.place import place_amenity
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place", secondary=place_amenity, backref="posts")
    name = ""
