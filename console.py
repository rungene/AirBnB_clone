#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon March 13 14:22:17 2023
@author: Clevers Rungene
         Lawrence Ongaki
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ A class containig the command interpreter entry"""
    prompt = '(hbnb)'

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
