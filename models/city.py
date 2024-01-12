#!/usr/bin/python3
"""Define the class for city"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class to represent city
        Public Attributes:
            state_id (str): it will be the satet_id: empty string
            name (str): empty-string
    """

    state_id = ""
    name = ""
