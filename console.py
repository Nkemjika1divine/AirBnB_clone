#!/usr/bin/python3
"""Tgis is the entry point of the AirBnB console. The console proper"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import cmd


class HBNBCommand(cmd.Cmd):
    """This is the console"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """this exits the console"""
        return True

    def do_EOF(self, arg):
        """This also exits the console"""
        return True

    def emptyline(self):
        """This emsures tgat nothing is don if whitespaces are entered"""
        pass

    def help_quit(self):
        """Print a custom help message when "help quit" is entered"""
        print("Quit command to exit the program\n")

    def do_create(self, arg):
        """This is used to create an instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        try:
            obj = arg.split()[0]  # store the first arg inobj
            instance = eval(obj)()  # evaluate & create instance of the class
            instance.save()  # call the save method on the created instance
            print(instance.id)  # print its id
        except (NameError, AttributeError):
            print("** class doesn't exist **")

    def do_show(self, arg):
        """This activates the show command
        it shows the dictionary reoresentation of the object"""
        if not arg:
            print("** class name missing **")
            return
        
        class_and_id = arg.split()
        if len(class_and_id) > 2:
            print("** instance id missing **")
            return

        class_var = class_and_id[0]
        id_var = class_and_id[1]



if __name__ == '__main__':
    HBNBCommand().cmdloop()
