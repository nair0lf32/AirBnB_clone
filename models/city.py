#!/usr/bin/python3
"""Defines City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """A class City that inherits from BaseModel"""
    state_id = ""
    name = ""
