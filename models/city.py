#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Monday March 13 05:55:43 2023
@authors: Clevers Rungene
          Lawrence
city module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherits from BaseModel

    Attributes:
        state_id: string - empty string: it will
        be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Init method for a class City

        Attributes:
            args(list): The list with arguments
            kwargs(dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
