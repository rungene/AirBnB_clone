#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon March 13 14:22:17 2023
@author: Clevers Rungene
         Lawrence Ongaki
"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ A class containig the command interpreter entry"""
    prompt = '(hbnb)'

    list_class = ['BaseModel']

    def do_EOF(self, args):
        """EOF to exit the program
        """
        return True

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """method does nothing when empty lines
        are inputted"""
        pass

    def postloop(self):
        """method to do nothing after each console loop
        """
        pass

    def do_create(self, args):
        """Create command to create a new instance of BaseModel, save it
        in a JSON file and prints the id

        Attributes:
            args(str) inputted line in a command prompt
        """
        my_args = args.split()
        if not self.class_exists(my_args):
            return
        instance = eval(line[0] + '()')
        if isinstance(instance, BaseModel):
            instance.save()
            print(instance.id)
        return

    def show(self, args):
        """Prints the string representation of an instance based on
        the class name and id

        Attributes:
            args(str) inputted line in command prompt
        """
        my_args = args.split()
        if not self.class_exists(my_args):
            return
        elif not self.id_exists(my_args):
            return
        key = '{}.{}'.format(line[0], line[1])
        objects = models.storage.all()
        print(objects[key])

    @classmethod
    def class_exists(cls, line):
        """class method that verifies inputted class"""
        if len(line) == 0:
            print('** class name missing **')
            return False
        elif line[0] not in HBNBCommand.list_class:
            print('** class doesn\'t exist **')
            return False
        return True

    @staticmethod
    def id_exists(line):
        """static method verifiess inputted instance id"""
        if len(line) < 2:
            print('** instance id missing **')
            return False
        objects = models.storage.all()
        key = '{}.{}'.format(line[0], line[1])
        if key not in objects.keys():
            print('** no instance found **')
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
