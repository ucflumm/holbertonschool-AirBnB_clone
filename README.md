<h1 align="center"> AirBnB Console </h1>

<div id="header" align="center">
<img src="https://m.media-amazon.com/images/M/MV5BZDIxZmY0YjgtMGZmMy00MDlmLWFjZmEtZTE4OWE2NmNlNGNlXkEyXkFqcGdeQXVyODExNTExMTM@._V1_.jpg" alt="luggage" width="400"/>
</div>

The console will be the backend to the larger Airbnb clone projcet. In this project we have built a base data model which has the ability to save objects in memory via a JSON file.



## Getting Started



Open your terminal and enter:

```
git clone https://github.com/ucflumm/holbertonschool-AirBnB_clone.git
```


## Usage
The command interpreter allows you to manipulate data without a visual interface. For the AirBnB clone, it allows you to create new objects, retrieve objects from files or databases, update object attributes, etc.

### Command Interpreter
The command interpreter can be used in two modes, interactive mode or non-interactive mode.
To start the command interpreter in the interactive mode you can run one of the following commands:

```
./console.py
```

or

```
python3 console.py
```

Once the command interpreter is running the the interactive mode, you can use the following commands:

|**Command**|**Description**|
|-----------|---------------|
|`create`| Creates a new instance of a class |
|`show`| Prints the instance with the class name and ID |
|`destroy`| Deletes an instance based on the class name and ID |
|`all`| Prints all instances |
|`update`| Updates an instance with an attribute based on the class name and ID |
|`help`| Displays a list of the available commands |
|`quit`| Exits the command interpreter |

In non-interactive mode, you can provide commands through a pipe or input redirection.

```
echo "all" | ./console.py
```

## Authors
- [Jessica Mo](https://github.com/jess6718)
- [Uwe Santos](https://github.com/ucflumm)
- [Duncan MacLennan](https://github.com/duncanmaclennan)