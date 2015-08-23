"""This file is to check how the colour-scheme looks with Python code
"""

# This is a comment, it should be slightly less contrasting than the rest of
# the text but should still be readable.

# Imports
import abc

# Constants
None, True, False
1, 1.0, 3j, 0xFF, 0o11
"string", "text\twith\u1011escapes\n", b"bytes", r"raw string", r"(?<=re)ge[x]{1}"


# Functions
def my_function(pos_param, pos_param_with_default=None):

    # Keywords
    if pos_param_with_default is None:
        return None

    # Built-in functions
    for i in range(100):
        print(i)

    # Operators
    print(1*2 + 3 - 4 ** 5 / 6)

    # Built-in types
    return str(int(pos_param))


class MyClass(object, metaclass=abc.ABCMeta):

    # Methods and Decorators
    @abc.abstractmethod
    def my_method(self, parameter):
        return parameter


class MyOtherClass(object, MyClass):
    """This is a nice thing! :P
    """

    def __init__(self, attribute):
        super().__init__()
        self.attribute = attribute

    def my_method(self, parameter):
        return super().my_method(parameter)
