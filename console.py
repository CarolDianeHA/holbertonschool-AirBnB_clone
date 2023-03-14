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
import shlex


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

    def do_create(self, arg):
        """Create a new object."""
        new = BaseModel()
        print(new.id)

    def do_show(self, arg):
        """Show name and id of the instance."""
        args_list = arg.split()
        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in classGroup.keys():
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[id_object])

    def do_destroy(self, arg):
        """Delete a given instance."""
        pass

    def do_all(self, arg):
        """Print a string representation of all instances."""
        pass

    def do_update(self, arg):
        """Update an instance with the information given."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
