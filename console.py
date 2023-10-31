#!/usr/bin/python3
"""
    Module: Console
    Description: Console for the AirBnB project
    Task docs say: no unit tests are required for the console
"""

# imports
import cmd
import io
import sys
# from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
        Class: HBNBCommand
        Description: Console for the AirBnB project
        Task docs: NO unit tests are required for the console
    """

    intro = None
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit(0)
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        sys.exit(0)
        return True

    def emptyline(self):
        """
            Overloading Cmd.emptyline()
            Action:
            Do nothing on empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
