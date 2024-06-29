#!/usr/bin/python3
""" This module contains the City class """
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base, State

class City(Base):
    """ The class City that inherits from Base, imported from model_state.

    Attributes:
        id: Not null, integer, auto-generate
        name: String of max length 128, not null
        state_id: Foreign key referencing states.id, not null
i    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
