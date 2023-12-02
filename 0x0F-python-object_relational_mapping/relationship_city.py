#!/usr/bin/python3
"""This module defines the City class with attributes id, name and state_id
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """The City class

    Attributes:
        id (int): The primary key for the city
        name (str): The name of the city
        state_id (int): foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
