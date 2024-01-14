#!/usr/bin/python3
"""Define the HBNBCommand Class"""
import cmd
import re
import json
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models import storage

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """A command that interprete class thta inherit from cmd.Cmd"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it and print the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel", "User", "Review", "State", "City",
                         "Place", "Amenity"]:
            print("** class doesn't exist **")
        else:
            obj = eval(arg)()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an\
                instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Review", "City", "State",
                             "Place", "Amenity"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            obj = storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and\
                id (save the change into the JSON file)."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all\
                instances based or not on the class name."""
        args = shlex.split(arg)
        obj_list = []

        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = {k: v for k, v in models.storage.all().items() if isinstance(v, classes[args[0]])}
        else:
            print("** class doesn't exist **")
            return False

        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))

        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "City", "State", "Amenity",
                             "Review", "Place"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            obj = storage.all().get(key)
            if obj:
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    attr_value = args[3]
                    if attr_name not in ["id", "created_at", "updated_at"]:
                        try:
                            attr_type = type(getattr(obj, attr_name))
                            attr_value = attr_type(attr_value)
                        except Exception as e:
                            pass
                        setattr(obj, attr_name, attr_value)
                        obj.save()
            else:
                print("** no instance is found **")

    def doquit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when the empty line is entered"""
        pass

    def help_quit(self):
        """Show the help message for the quit command"""
        print("Quit command to exit the program")

    def help_create(self):
        """Show the help message for the create command"""
        print("Create a new instance of BaseModel, save it and print the id")
        print("Usage: create <class name>")

    def help_show(self):
        """Show the help message for the show command"""
        print("Print the string representation of an\
                instance based on the class name and id")
        print("Usage: show <class name> <id>")

    def help_destroy(self):
        """Show the help message for the destroy command"""
        print("Delete an instance based on the class name and id")
        print("Usage: destroy <class name> <id>")

    def help_all(self):
        """Show the help message for the all command"""
        print("Print all string representation of all\
                instances based or not on the class name")
        print("Usage: all <class name> (optional)")

    def help_updat(self):
        """Show the help message for the update command"""
        print("Update an instance based on the class name and\
                id by adding or updating attribute")
        print("Usage: update <class name> <id> <attribute\
                name> \"<attribute value>\"")

        def help_EOF(self):
            """show the help mesaage for EOF command"""
        print("EOF command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
