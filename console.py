#!/usr/bin/python3
import cmd
import models
import shlex
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
        "Place": Place, "Review": Review, "State": State, "User": User}

class HBNBCommand(cmd.Cmd):
    """Cmd clone"""
    # intro = """Documented commands (type help <topic>):\n========================================\nEOF\t  help\t  quit\n \n"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit console"""
        return True

    def emptyline(self):
        """empty line. Do nothing"""
        return False

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """

        # TODO: make this common check a property
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] in classes:
            new_dict = self.key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class `name` and `id`
        """
        agrs = shlex.split(arg)
        if len(arg) == 0:
            print('** class name missing **')
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in model.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = shlex.split(args)
        if len(args) == 0:
            print('** class name missing **')
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
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")


    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
            print("** class doesn't exist **")

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
