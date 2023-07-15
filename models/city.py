#!/usr/bin/python3
"""Module to create a User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for city objects"""

    state_id = ""
    name = ""
