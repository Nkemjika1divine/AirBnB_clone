#!/usr/bin/python3
"""Tgis is the entry point of the AirBnB console. The console proper"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
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
        if len(class_and_id) < 2:
            class_var = class_and_id[0]

            everything = storage.all()
            class_list = []
            for i in everything:
                class_name = i.split(".")[0]
                class_list.append(class_name)
            if class_var not in class_list:
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
            everything = storage.all()
            class_list = []
            for i in everything:
                class_name = i.split(".")[0]
                class_list.append(class_name)
            if class_var not in class_list:
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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
