#!usr/bin/python3
"""Module review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines Review class that inherit from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
