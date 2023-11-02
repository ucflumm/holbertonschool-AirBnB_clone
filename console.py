#!/usr/bin/python3
"""
    Module: Console.py
    Description: Console for the AirBnB project
    Task docs say: no unit tests are required for the console
"""

# imports
import cmd
import io
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        Class: HBNBCommand
        Description: Console for the AirBnB project
        Task docs: NO unit tests are required for the console
    """
    storage.reload()
    intro = None
    prompt = '(hbnb) '
    # would be good to get dynamic updating of this list
    # possibly if class_name in globals()
    # or something like that
    class_dict = {"BaseModel": BaseModel}
    # Probably need to add all the other classes here

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit(0)
        return True

    def do_exit(self, arg):
        """Exit command to exit the program"""
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

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
            Prints the string representation of an instance
            based on the class name and id
        """
        arg_list = arg.split()
        if len(arg[0]) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            try:
                key = "{}.{}".format(arg_list[0], arg_list[1])
                key in storage.all()
                print(storage.all()[key])
            except NameError:
                print("** no instance found **")
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
            (save the change into the JSON file)
        """
        arg_list = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            try:
                key = "{}.{}".format(arg_list[0], arg_list[1])
                key in storage.all()
                del storage.all()[key]
                storage.save()
            except NameError:
                print("** no instance found **")
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name
        """
        arg_list = arg.split()
        if len(arg_list) == 0:
            for key, value in storage.all().items():
                print(value)
        elif arg not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if arg == key.split(".")[0]:
                    print(value)

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id
        """
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key not in storage.all():
                print("** no instance found **")
            elif len(arg_list) <= 2:
                print("** attribute name missing **")
            elif len(arg_list) <= 3:
                print("** value missing **")
            else:
                setattr(storage.all()[key], arg_list[2], arg_list[3])
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
