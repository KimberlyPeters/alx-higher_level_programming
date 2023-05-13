# Python - Data Structures: Lists, Tuples

In this project, I learned about how sequence data types work in
Python - specifically, lists and tuples.


## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                               | Prototype                                      |
| ---------------------------------- | ---------------------------------------------- |
| `0-print_list_integer.py`          | `def print_list_integer(my_list=[]):`          |
| `1-element_at.py`                  | `def element_at(my_list, idx):`                |
| `2-replace_in_list.py`             | `def replace_in_list(my_list, idx, element):`  |
| `3-print_reversed_list_integer.py` | `def print_reversed_list_integer(my_list=[]):` |
| `4-new_in_list.py`                 | `def new_in_list(my_list, idx, element):`      |
| `5-no_c.py`                        | `def no_c(my_string):`                         |
| `6-print_matrix_integer.py`        | `def print_matrix_integer(matrix=[[]]):`       |
| `7-add_tuple.py`                   | `def add_tuple(tuple_a=(), tuple_b=()):`       |
| `8-multiple_returns.py`            | `def multiple_returns(sentence):`              |
| `9-max_integer.py`                 | `def max_integer(my_list=[]):`                 |
| `10-divisible_by_2.py`             | `def divisible_by_2(my_list=[]):`              |
| `11-delete_at.py`                  | `def delete_at(my_list=[], idx=0):`            |
| `100-print_python_list_info.c`     | `void print_python_list_info(PyObject *p);`    |

## Tasks :page_with_curl:

* **0. Print a list of integers**
  * [0-print_list_integer.py](./0-print_list_integer.py): Python function that prints all
  integers of a list, one per line.
  * Without importing modules or casting integers into strings.

* **1. Secure access to an element in a list**
  * [1-element_at.py](./1-element_at.py): Python function that retrieves an element
  from a list.
  * If `idx` is negative or out of range (greater than the number of elements in
  `my_list`), the function returns `None`.
  * Without import modules or using `try/except`.
