#!/usr/bin/python3
"""
program used to handle user data
"""
from models.base_model import BaseModel
class User(BaseModel):
    """
    handles user information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""


