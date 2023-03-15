#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Monday March 13 05:55:43 2023
@authors: Clevers Rungene
          Lawrence
user module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel

    Attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Init method for a class User

        Attributes:
            args(list): The list with arguments
            kwargs(dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
