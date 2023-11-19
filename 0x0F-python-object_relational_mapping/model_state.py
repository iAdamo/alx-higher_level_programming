#!/usr/bin/python3
"""
This module defines the State class with attributes id and name.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class inherits from Base. This class links to the MySQL table states.
    Attributes:
        id: Represents a column of an integer type, is a primary key, can't be
        null and is unique.
        name: Represents a column of a string type.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(255))
