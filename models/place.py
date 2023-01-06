#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
from models.base_model import BaseModel, Base
from models.review import Review
import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == 'db':
    metadata = Base.metadata
    place_amenity = Table("place", metadata, Column(
        'place_id', String(60), ForeignKey('places.id'), nullable=False), Column(
        'amenity_id', String(60), ForeignKey('amenities.id'), nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)

        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @ property
        def reviews(self):
            '''Getter function for reviews'''
            list_reviews = []
            all_reviews = models.storage.all(Review)
            for _, review in all_reviews:
                if review.place_id == self.id:
                    list_reviews.append(review)
            return list_reviews
