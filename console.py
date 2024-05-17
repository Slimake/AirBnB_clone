#!/usr/bin/python3
"""Module console.py"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True
    
    def emptyline(self):
        pass

    def help_quit(self):
        print("Quit command to exit the program\n")
    
    def help_EOF(self):
        print("Quit command to exit the program\n")
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()