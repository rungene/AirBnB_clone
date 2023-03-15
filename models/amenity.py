#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Monday March 13 05:55:43 2023
@authors: Clevers Rungene
          Lawrence
Amenity module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity that inherits from BaseModel

    Attributes
        name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Init method for a class Amenity

        Attributes:
            args(list): The list with arguments
            kwargs(dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
