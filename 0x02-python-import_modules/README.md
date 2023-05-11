# Python - import & modules

In this project, I learned about importing and using functions and creating
modules in Python. I further practiced using the builtin function
`dir()` and using command line arguments within Python programs.

## Tasks :page_with_curl:

* **0. Import a simple function from a simple file**
  * [0-add.py](https://github.com/KimberlyPeters/alx-higher_level_programming/blob/master/0x02-python-import_modules/0-add.py): Python program that imports the function `def add(a, b):` from the file [add_0.py](https://github.com/KimberlyPeters/alx-higher_level_programming/blob/master/0x02-python-import_modules/add_0.py) and prints the result of the addition `1 + 2 = 3`.
  * Output: `<a value> + <b value> = <add(a, b) value>` followed by a new line.

* **1. My first toolbox!**
  * [1-calculation.py](https://github.com/KimberlyPeters/alx-higher_level_programming/blob/master/0x02-python-import_modules/1-calculation.py): Python program that imports functions
  from the file [calculator_1.py](https://github.com/KimberlyPeters/alx-higher_level_programming/blob/master/0x02-python-import_modules/calculator_1.py) and prints the result
  of the addition, subtraction, multiplication and division of `10` and `5`.
  * Output: `<a value> <operator> <b value> = <operation(a, b) value>` followed by a new line.

* **2. How to make a script dynamic!**
  * [2-args.py](https://github.com/KimberlyPeters/alx-higher_level_programming/blob/master/0x02-python-import_modules/2-args.py): Python program that prints the number of
  and list of its arguments.
  * Output: `[Number of arguments] argument` (if number is one) or `arguments` (otherwise), followed by:
    * `:` (or `.` if no argumets were passed), followed by
    * A new line, followed by
    * One argument per line - the position of the argument (starting at `1`) followed by `:` followed by the argument value and another new line.

* **3. Infinite addition**
  * [3-infinite_add.py](https://github.com/KimberlyPeters/alx-higher_level_programming/blob/master/0x02-python-import_modules/3-infinite_add.py): Python program that prints the result of the
  addition of all arguments.
  * Output: Sum of the arguments followed by a new line.

* **4. Who are you?**
  * [4-hidden_discovery.py](https://github.com/KimberlyPeters/alx-higher_level_programming/blob/master/0x02-python-import_modules/4-hidden_discovery.py): Python program that prints all the
  names defined by the compiled module [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc).
  * Output: One name per line in alphabetical order.
  * Names starting with `__` are not printed.
