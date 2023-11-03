#!/usr/bin/python3
"""

module wuich contains that function that adds two numbers

"""


def add_integer(a, b=98):
    """ this function adds two integer or float numbers

    Args:
        a: the first number
        b: the second number

    Returns:
         adds any two given numbers
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
