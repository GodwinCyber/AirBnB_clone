#!/usr/bin/python3
"""Defines review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class representing review
        Public attributes
            place_id (str): it will be place_id: empty string
            user_id (str): it will be user_id: empty string
            text (str): empty string
    """

    place_id = ""
    user_id = ""
    text = ""
