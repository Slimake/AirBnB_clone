### Airbnb clone

#### Description

> Airbnb Clone: The console is the first phase of the project. This repository contains the command interpreter (HBNBCommand class that inherit from cmd.Cmd class), the BaseModel class and several other classes such as Amenity, City, State, Place, Review.

#### How to use the Command Interpreter

---

| Commands      | How to use it                    | What it does                                                                     |
| ------------- | -------------------------------- | -------------------------------------------------------------------------------- |
| `help`        | `help or ?`                      | to list available commands                                                       |
| `create`        | `create <classname>`           | Creates a new instance of BaseModel and prints the id                            |
| `show`        | `show <classname> <id>`          | Prints the string representation of an instance based on the class name and id   |
| `destroy`     | `destroy <classname> <id>`       | Deletes an instance based on the class name and id                               |
| `all`         | `all or all <classname>`         | Prints all string representation of all instances based or not on the class name |
| `update`      | `update <class name> <id> <attr name> <attr value>` | Updates an instance based on the class name and id            |    

#### Installation
```
git clone https://github.com/Slimake/AirBnB_clone.git
cd AirBnB_clone
```

#### Execution
Interactive Mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help quit
Quit command to exit the program

(hbnb) quit
$
```

Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

#### Environment
* OS: Ubuntu 20.04 LTS
* Language: Python
* Version: 3.8.5
* Style Guide: [Python](https://pypi.org/project/pycodestyle/) (v2.8.*)

## Authors
[Twitter](https://twitter.com/slimake)