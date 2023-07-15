#!/usr/bin/python3
"""Module to create a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
