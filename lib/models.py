#!/usr/bin/env python3

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base  # Updated import

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer, primary_key=True)  # No need for parentheses
    name = Column(String)
    breed = Column(String)
