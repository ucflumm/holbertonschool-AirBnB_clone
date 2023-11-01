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
            except:
                print("** class doesn't exist **")

    def do_show(self, *arg):
        """
            Prints the string representation of an instance
            based on the class name and id
        """
        if len(arg[0]) == 0:
            print("** class name missing **")
        else:
            if ' ' not in arg[0]:
                print(arg[1])
                print("** instance id missing **")
            else:
                class_name, id = arg[0].split(" ")
                try:
                    key = class_name + "." + id
                    key in storage.all()
                    print(storage.all()[key])
                except:
                    print("** no instance found **")

    def do_destroy(self, *arg):
        """
            Deletes an instance based on the class name and id
            (save the change into the JSON file)
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            class_name = arg[0].split(".")[0]
            id = arg[0].split(".")[1]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                key = class_name + "." + id
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
            Prints all string representation of all instances
        """

        if len(arg) == 0:
            print([str(value) for value in storage.all().values()])
        else:
            class_name = arg.split(".")[0]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                print([str(value) for key, value in storage.all().items()
                      if key.startswith(class_name)])

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            class_name = arg.split(".")[0]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                id = arg.split(".")[1]
                key = class_name + "." + id
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    if len(arg.split(".")) == 2:
                        print("** attribute name missing **")
                    elif len(arg.split(".")) == 3:
                        print("** value missing **")
                    else:
                        attr_name = arg.split(".")[2]
                        attr_value = arg.split(".")[3]
                        setattr(storage.all()[key], attr_name, attr_value)
                        storage.all()[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
