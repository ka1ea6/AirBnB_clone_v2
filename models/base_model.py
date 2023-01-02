#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and isinstance(self.created_at, str):
                self.created_at = datetime.strptime(
                    kwargs["created_at"], time_format)
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", None) and isinstance(self.updated_at, str):
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], time_format)
            else:
                self.updated_at = datetime.now()

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        # cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        if isinstance(self.updated_at, str):
            dict_copy["updated_at"] = self.updated_at.strftime(time_format)
        if isinstance(self.created_at, str):
            dict_copy["created_at"] = self.created_at.strftime(time_format)
        if '_sa_instance_state' in dict_copy:
            del dict_copy['_sa_instance_state']

        # dictionary.update(self.__dict__)
        # dictionary.update({'__class__':
        #                   (str(type(self)).split('.')[-1]).split('\'')[0]})
        # dictionary['created_at'] = self.created_at.isoformat()
        # dictionary['updated_at'] = self.updated_at.isoformat()

        return dict_copy

    def delete(self):
        '''deletes the current instance from the storage'''
        models.storage.delete(self)
