#!/usr/bin/python3
"""Defines HBNBCommand class"""


from models import storage
import cmd
from models.base_model import BaseModel
from models.user import User

from shlex import split


def parse(argv):
    return [i.strip(",") for i in split(argv)]


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = "(hbnb) "
    _class = ["BaseModel", "User"]

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        Ex: $ create BaseModel"""

        argv = parse(line)
        if argv == []:
            print("** class name missing **")
        elif argv[0] in HBNBCommand._class:
            new = eval(argv[0])()
            storage.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234."""

        argv = parse(line)
        if argv == []:
            print("** class name missing **")
        elif argv[0] in HBNBCommand._class:
            if len(argv) == 1:
                print("** instance id missing **")
            else:
                show_key = argv[0] + "." + argv[1]
                if show_key in storage.all().keys():
                    print(storage.all()[show_key])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234."""

        argv = parse(line)
        if argv == []:
            print("** class name missing **")
        elif argv[0] in HBNBCommand._class:
            if len(argv) == 1:
                print("** instance id missing **")
            else:
                destroy_key = argv[0] + "." + argv[1]
                if destroy_key in storage.all().keys():
                    del storage.all()[destroy_key]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name.
        Ex: $ all BaseModel or $ all"""

        argv = parse(line)
        if argv == []:
            print([str(v) for v in storage.all().values()])
        elif len(argv) == 1:
            if argv[0] in HBNBCommand._class:
                print(
                    [str(v) for v in storage.all().values()
                        if v.to_dict()["__class__"] == argv[0]])
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""

        argv = parse(line)
        if argv == []:
            print("** class name missing **")
        elif len(argv) >= 1:
            if argv[0] in HBNBCommand._class:
                if len(argv) >= 2:
                    update_key = argv[0] + "." + argv[1]
                    if update_key in storage.all().keys():
                        if len(argv) >= 3:
                            if len(argv) >= 4:
                                setattr(storage.all()[update_key],
                                        argv[2], argv[3])
                                storage.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def emptyline(self):
        """Handle an empty line + ENTER"""
        pass

    def do_EOF(self, line):
        """The end-of-file marker"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        raise SystemExit


if __name__ == "__main__":
    HBNBCommand().cmdloop()
