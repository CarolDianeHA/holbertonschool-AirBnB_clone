#!/usr/bin/env python3
"""This module implements the command interpreter."""

import cmd
from models.base_model import BaseModel


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
        print(new)

    def do_show(self, arg):
        """Show name and id of the instance."""
        pass

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
