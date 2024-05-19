#!usr/bin/python3
"""Module user"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines User class that inherit from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
