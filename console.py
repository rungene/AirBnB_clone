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
        instance = eval(my_args[0] + '()')
        if isinstance(instance, BaseModel):
            instance.save()
            print(instance.id)
        return

    def do_show(self, args):
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
        key = '{}.{}'.format(my_args[0], my_args[1])
        objects = models.storage.all()
        print(objects[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name
        and id

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
        del objects[key]
        models.storage.save()

    def do_all(self, args):
        """ Prints all string representation of all instances
        based or not on the class name.

        Attributes:
            args(str) inputted line in command prompt
        """
        my_args = args.split()
        objects = models.storage.all()
        to_print = []
        if len(my_args) == 0:
            for v in objects.value():
                to_print.append(str(v))
        elif my_args[0] in HBNBCommand.list_class:
            for k, v in objects.items():
                if my_args[0] in k:
                    to_print.append(str(v))
        else:
            print("** class doesnt exist **")
            return False
        print(to_print)

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).

        Attrribute:
            args (str): inputted line in command prompt.
        """
        my_args = args.split()
        if not self.class_exists(my_args):
            return
        elif not self.id_exists(my_args):
            return
        elif not self.attribute_exists(my_args):
            return
        objects = models.storage.all()
        key = '{}.{}'.format(my_args[0], my_args[1])
        setattr(objects[key], my_args[2], my_args[3])
        models.storage.save()

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

    @staticmethod
    def attribute_exists(line):
        """static method verifies inputted instance attribute"""
        if len(line) < 3:
            print("** attribute name missing **")
            return False
        elif len(line) < 4:
            print("** value missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
