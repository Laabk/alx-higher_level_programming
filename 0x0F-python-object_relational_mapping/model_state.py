#!/usr/bin/python3
"""
a script which defines a City class
to work with MySQLAlche.
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

class CityBbase):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=Fa
