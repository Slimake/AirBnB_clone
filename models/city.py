#!usr/bin/python3
"""Module city"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines City class that inherit from BaseModel"""

    state_id = ""
    name = ""
