#!/usr/bin/python3
"""Module console"""

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
            classes = ["BaseModel", "User"]
            obj_list = []
            for key in dic.keys():
                dic_classname = key.split(".")[0]

                if dic_classname == line:
                    obj = dic[key]
                    obj_list.append(str(obj))

            if line not in classes:
                print("** class doesn't exist **")
                return
            print(obj_list)
            return
        else:
            for obj in dic.values():
                obj_list.append(str(obj))
            print(obj_list)
            return

    def do_create(self, line):
        from models.base_model import BaseModel
        from models.user import User

        fs = FileStorage()
        dic = fs.all()
        classname = ""

        if line:
            classes = {
                "BaseModel": BaseModel,
                "User": User
            }

            for name, value in classes.items():
                if name == line:
                    classname = value
                elif name == line:
                    classname = value
                else:
                    if line not in classes:
                        print("** class doesn't exist **")
                        return
        else:
            print("** class name missing **")
            return

        bm = classname()
        bm.save()
        print(bm.id)

    def do_destroy(self, line):
        fs = FileStorage()
        dic = fs.all()
        args = line.split()

        try:
            classname = args[0]
            _id = args[1]
        except IndexError:
            if len(args) == 0:
                classname = None
            elif len(args) == 1:
                _id = None

        if classname is not None:
            classes = []
            for key in dic.keys():
                dic_classname = key.split(".")[0]
                if dic_classname not in classes:
                    classes.append(dic_classname)

            if classname not in classes:
                print("** class doesn't exist **")
                return
        else:
            print("** class name missing **")
            return

        if _id is not None:
            key = classname + "." + _id
            if key not in dic.keys():
                print("** no instance found **")
                return
        else:
            print("** instance id missing **")
            return

        del dic[key]
        fs.save()
        return

    def do_show(self, line):
        fs = FileStorage()
        dic = fs.all()
        args = line.split()

        try:
            _classname = args[0]
            _id = args[1]
        except IndexError:
            if len(args) == 0:
                print("** class name missing **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return

        classes = []
        for key in dic.keys():
            dic_classname = key.split(".")[0]
            if dic_classname not in classes:
                classes.append(dic_classname)

        if _classname not in classes:
            print("** class doesn't exist **")
            return

        if _id is not None:
            key = _classname + "." + _id
            if key in dic.keys():
                obj = dic[key]
                print(obj)
                return
            else:
                print("** no instance found **")
                return
        else:
            print("** instance id missing **")
            return

    def do_update(self, line):
        fs = FileStorage()
        dic = fs.all()
        args = line.split()

        try:
            _class = args[0]
            _id = args[1]
            _attr_name = args[2]
            _attr_val = args[3]
        except IndexError:
            if len(args) == 0:
                _class = None
            elif len(args) == 1:
                _id = None
            elif len(args) == 2:
                _attr_name = None
            elif len(args) == 3:
                _attr_val = None

        if _class is not None:
            classes = []
            for key in dic.keys():
                classname = key.split(".")[0]
                if classname not in classes:
                    classes.append(classname)
            if _class not in classes:
                print("** class doesn't exist **")
                return
        else:
            print("** class name missing **")
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
                setattr(inst, _attr_name, str(_attr_val[1:-1]))
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
