#!/usr/bin/python3
"""Defines HBNBCommand class"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Handle an empty line + ENTER"""
        pass

    def do_EOF(self, argv):
        """The end-of-file marker"""
        print()
        return True

    def do_quit(self, argv):
        """Quit command to exit the program"""
        raise SystemExit


if __name__ == "__main__":
    HBNBCommand().cmdloop()
