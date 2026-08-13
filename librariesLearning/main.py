# module is a file containing Python code that can be imported and used in other Python programs. 
# Modules allow you to organize your code into separate files, making it easier to manage and reuse.
# each module contains one task

import math_utils
import math
import random
import datetime

print(math_utils.add_numbers(10, 5))  # Output: 15
print(math_utils.subtract_numbers(10, 5))  # Output: 5

print(math.sqrt(16))  # Output: 4.0
print(random.randint(1, 10))  # Output: a random integer between 1 and 10
print(datetime.datetime.now())  # Output: current date and time

# a package is a folder that contains multiple modules.
# when the file `__init__.py` is present in a folder, it is treated as a package.

# check lecture1.py for import packages.

