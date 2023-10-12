#!/usr/bin/python3
"""Tgis is the entry point of the AirBnB console. The console proper"""
import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """This is the console"""
    prompt = "(hbnb) "
    classes = {
            "BaseModel": BaseModel,
            "FileStorage": FileStorage,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

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

    def help_EOF(self):
        """Custom message that shows what EOF does"""
        print("EOF exits the console")

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

    def help_create(self):
        """This explains what the create command does"""
        print("enter [create <class name>] to create an instance of the class")

    def do_show(self, arg):
        """This activates the show command
        it shows the dictionary reoresentation of the object"""
        if not arg:
            print("** class name missing **")
            return
        
        class_and_id = arg.split()
        if len(class_and_id) < 2:
            class_var = class_and_id[0]
            if class_var not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return
        else:
            class_var = class_and_id[0]
            id_var = class_and_id[1]
            clsname_id = "{}.{}".format(class_var, id_var)
            everything = storage.all()
            if clsname_id not in everything:
                print("** no instance found **")
                return

        print(everything[clsname_id])
    
    def do_destroy(self, arg):
        """This deletes an instance of an object"""
        if not arg:
            print("** class name missing **")
            return

        class_and_id = arg.split()
        if len(class_and_id) < 2:
            class_var = class_and_id[0]
            if class_var not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return
        else:
            class_var = class_and_id[0]
            id_var = class_and_id[1]
            everything = storage.all()
            clsname_id = "{}.{}".format(class_var, id_var)
            if clsname_id not in everything:
                print("** no instance found **")
                return

        del storage.all()[clsname_id]
        storage.save()

    def do_all(self, arg):
        """This activates the all command
        it shows all instances, or all instances of a class"""
        everything = storage.all()
        if not arg:
            print_val = []
            for key, value in everything.items():
                print_val.append("{}".format(value))
            print(print_val)
            return

        class_name = arg.split()[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        print_val = []
        for key, value in everything.items():
            if class_name == key.split(".")[0]:
                print_val.append("{}".format(value))
        print(print_val)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
