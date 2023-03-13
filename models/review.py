#!/usr/bin/pyhton3
"""Review class module."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class methods."""

    place_id = ""
    user_id = ""
    text = ""
