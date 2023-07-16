<p align="center">
  <img src="https://github.com/edward0rtiz/AirBnB_clone/blob/master/hbton.png" alt="Hbton logo">
</p>

<p align="left"> AirBnB clone project</p>
---
## Description
Airbnb Clone is a web app with full development of back-end and front-end API
integrating also SQL storage 
This project is part 1 of 4 in which the back-end console is created
and deployed.
This is an educational purpose clone from [AirBnB](https://www.airbnb.com/)

## Classes

This project uses the following classes:

BaseModel
User
Amenity
City
Place
State
Review

## Storage

The presented classes are stored in the [FileStorage](./models/engine/file_storage.py) class file.
When the console is initialized, the console redirects an instance of
FileStorage is named storage.
#Storage object is loaded or reloaded from any class instances stored in the
JSON file file.json.
Class instances are created, updated, or deleted, and storage object registers
changes intofile.json.

## Console
The console is a CLI that allows the use of data as a backend tool.
It can be used to handle all classes predefined previously called into
`storage` objects.

### How to Use the CLI Non-interactive
To run the console in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
$
```

### How to Use the CLI interactive
To run the console in an interactive mode:

run the file console.py:

```
$ ./console.py
```

To quit the console, enter the command `quit`, or input an EOF signal
(`ctrl-D`).

### Console Commands
Airbnb supports the following commands:
 **create**
  * Usage: create <class>
Creates a new instance of a given class. Class ID is printed and
the instance is saved to the file file.json.

 **show**
  * Usage: show <class> <id> or <class>.show(<id>)
Prints a string representation of a class instance based on a given id.

* **destroy**
  * Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`
Deletes a class instance based on a given id from the storage file file.json and
it is updated accordingly.

 **all**
  * Usage: all or all <class> or <class>.all()
Prints the string representations of all instances of a given class. If no
class name is provided, the command prints all instances of every class.

 **count**
  * Usage: `count <class>` or `<class>.count()`
Retrieves the number of instances of a given class.

 **update**
  * Usage: update <class> <id> <attribute name> "<attribute value>"` or
`<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(
<id>, <attribute dictionary>).
Updates a class instance based on a given id with a given key/value attribute	
pair or dictionary of attribute pairs. If an update is called with a single 
key/value attribute pair, only "simple" attributes can be updated (ie. not 
id, created_at, and/or updated_at).

## How to Test:
Unittests for the CLI HolbertonBnB project are defined in the [tests](./tests)
folder. To run the entire test suite simultaneously, execute the following
command:

```
$ python3 unittest -m discover tests
```

Also, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## Authors:
**Tokallah Hussein** <[Tokaallah](https://github.com/Tokaallah)>
**Shady Egypt** <[Shady Egypt](https://github.com/ShadyEgypt)>
