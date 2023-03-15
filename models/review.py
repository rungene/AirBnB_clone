#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Monday March 13 05:55:43 2023
@authors: Clevers Rungene
          Lawrence
Review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits from BaseModel

    Attributes:
        place_id: string - empty string: it will
        be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Init method for a class Review

        Attributes:
            args(list): The list with arguments
            kwargs(dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
