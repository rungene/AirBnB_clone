#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Monday March 13 05:55:43 2023
@authors: Clevers Rungene
          Lawrence
state module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class State that inherits frmo BaseModel

    Attribute:
        name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Init method for a class User

        Attributes:
            args(list): The list with arguments
            kwargs(dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
