#!/usr/bin/env python3
"""This module implements the command interpreter."""

import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models


classGroup = {"Amenity": Amenity, "BaseModel": BaseModel,
              "City": City, "Place": Place, "Review": Review,
              "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """This class defines the command interpreter."""

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, line):
        """Create a new object."""
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classGroup.keys():
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            print(new.id)
            models.storage.save()

    def do_show(self, arg):
        """Show name and id of the instance."""
        args_list = arg.split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in classGroup.keys():
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        else:
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[id_object])

    def do_destroy(self, arg):
        """Delete a given instance."""
        args_list = arg.split()
        if len(args_list) == 0:
            print(" ** class name missing ** ")
        elif args_list[0] not in classGroup.keys():
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        else:
            id_object = f"{args_list[0]}.{args_list[1]}"
            data = models.storage.all()
            if id_object in data:
                del data[id_object]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print a string representation of all instances."""
        all_list = []

        if arg:
            split = arg.split(" ")[0]
            if arg not in classGroup:
                print("** class doesn't exist **")
                return False
            data = models.storage.all()
            for key, value in data.items():
                all_list.append(str(value))
            else:
                print(all_list)

    def do_update(self, arg):
        """Update an instance with the information given."""
        if not arg:
            print("** class name missing **")
            return
        args_list = arg.split()
        if args_list[0] not in classGroup.keys():
            print("** class doesn't exist **")
            return

        try:
            args = arg.split()
            obj_dict = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in obj_dict:
                print("** no instance found **")
                return

            obj = obj_dict[key]
            if len(args) == 2:
                print("** attribute name missing **")
                return
            if len(args) == 3:
                print("** value missing **")
                return

            setattr(obj, args[2], type(getattr(obj, args[2]))(args[3]))
            obj.save()
        except AttributeError:
            obj.save.append()
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
