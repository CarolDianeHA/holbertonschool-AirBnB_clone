# AirBnB clone project/Console

![logo](https://github.com/CarolDianeHA/holbertonschool-AirBnB_clone/blob/caroldiane/image/hbnb%20logo.png)

## Project Description

The end goal of the project is to deploy on your server a simple copy of the [AirBnB website](https://www.airbnb.com/). This phase just will complete the console.

Web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

Next Phases:

* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

### General Concepts

* Unittest - and please work all together on tests cases
* Python packages concept page
* Serialization/Deserialization (Json)
* `*args`, `**kwargs`
* datetime

### Diagram

![diagram](https://github.com/CarolDianeHA/holbertonschool-AirBnB_clone/blob/caroldiane/image/Project%20Diagram.png)

## Console commands

* `create` - Creates a new instance of BaseMode, saves it to Json file, prints id and manage some errors.
* `show` - Prints the string representation of an instance based on the class name and id.
* `destroy` - Deletes an instance based on the class name and id, and saves the change into the Json file.
* `all` - Prints all string representation of all instances based or not on the class name.
* `update`- Updates an instance based on the class name and id by adding or updating attributes, and save the changes into the Json file.

## Execution

The shell should work like this in interactive mode:

```py
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode:

```py
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

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

## Authors

* Carol Diane Hernández |   <img alt="GitHub" width="26px" src="https://raw.githubusercontent.com/github/explore/78df643247d429f6cc873026c0622819ad797942/topics/github/github.png" /> [GitHub](https://github.com/CarolDianeHA) |

* Abigail Castro | <img alt="GitHub" width="26px" src="https://raw.githubusercontent.com/github/explore/78df643247d429f6cc873026c0622819ad797942/topics/github/github.png" />[GitHub](https://github.com/AbigailCastroFigueroa) |
