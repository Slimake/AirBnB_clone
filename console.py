#!/usr/bin/python3
"""Module console.py"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_all(self, line):
        obj_list = []
        fs = FileStorage()
        dic = fs.all()

        if line:
            if line != "BaseModel":
                print("** class doesn't exist **")
                return
            
            for key in dic.keys():
                key_list = key.split(".")
                if key_list[0] == "BaseModel":
                    obj = dic[key]
                    obj_list.append(str(obj))
            print(obj_list)
        else:
            for obj in dic.values():
                obj_list.append(str(obj))
            print(obj_list)

    def do_create(self, line):
        if line:
            if line == "BaseModel":
                bm = BaseModel()
                bm.save()
                print(bm.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        line_list = line.split()

        if not line:
            print("** class name missing **")
            return
        if line_list[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        
        try:
            if line_list[1]:
                fs = FileStorage()
                dic = fs.all()
                for key in dic.keys():
                    key_list = key.split(".")
                    if line_list[1] == key_list[1]:
                        del dic[key]
                        fs.save()
                        return
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

    def do_show(self, line):
        line_list = line.split()

        if not line:
            print("** class name missing **")
            return
        if line_list[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        try:
            if line_list[1]:
                fs = FileStorage()
                dic = fs.all()
                for key in dic.keys():
                    key_list = key.split(".")
                    if line_list[1] == key_list[1]:
                        obj = dic[key]
                        print(obj)
                        return
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

    def do_update(self, line):
        fs = FileStorage()
        dic = fs.all()
        args = line.split()

        try:
            _class = args[0]
            _id = args[1]
            _attr_name = args[2]
            _attr_val = args[3]
        except:
            if len(args) == 0:
                _class = None
            elif len(args) == 1:
                _id = None
            elif len(args) == 2:
                _attr_name = None
            elif len(args) == 3:
                _attr_val = None
            elif len(args) == 4:
                pass

        if _class is not None:
            classes = []
            for key in dic.keys():
                classname = key.split(".")[0]
                if classname not in classes:
                    classes.append(classname)
        else:
            print("** class name missing **")
            return

        if _class not in classes:
            print("** class doesn't exist **")
            return
        
        if _id is not None:
            key = _class + "." + _id
            if key not in dic.keys():
                print("** no instance found **")
                return
        else:
            print("** instance id missing **")
            return
            
        if _attr_name is None:
            print("** attribute name missing **")
            return
        
        if _attr_val is None:
            print("** value missing **")
            return
        
        key = _class + "." + _id
        inst = dic[key]
        if hasattr(inst, _attr_name):
            attr_type = type(getattr(inst, _attr_name))

            if attr_type == str:
                setattr(inst, _attr_name, str(_attr_val))
            elif attr_type == int:
                setattr(inst, _attr_name, int(_attr_val))
            elif attr_type == float:
                setattr(inst, _attr_name, float(_attr_val))
        else:
            try:
                _attr_val = float(_attr_val)
                if _attr_val.is_integer():
                    raise ValueError
            except (ValueError, OverflowError):
                try:
                    _attr_val = int(_attr_val)
                except ValueError:
                    _attr_val = str(_attr_val[1:-1])
            setattr(inst, _attr_name, _attr_val)
        inst.save()

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def help_all(self):
        print("Prints all string representation of all "
                "instances based or not on the class name. ")

    def help_create(self):
        print("Creates a new instance of BaseModel, saves it "
                "(to the JSON file) and prints the id.")

    def help_destroy(self):
        print("Deletes an instance based on the class name and "
                "id (save the change into the JSON file).")

    def help_update(self):
        print("Updates an instance based on the class name "
                "and id by adding or updating attribute "
                    "(save the change into the JSON file). ")
        
    def help_show(self):
        print("Prints the string representation of "
                "an instance based on the class name and id.")
        
    def help_EOF(self):
        print("Quit command to exit the program\n")

    def help_quit(self):
        print("Quit command to exit the program\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
