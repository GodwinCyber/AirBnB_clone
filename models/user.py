#!/usr/bin/python3
"""Define the users class"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class to represent a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
