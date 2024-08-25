'''
Fibonacci - A Python Library for Fibonacci Numbers

This library provides a simple interface for calculating Fibonacci numbers.
It supports both small and large numbers, and provides a variety of
options for customization.

Usage:

>>> from fibonacci import fibonacci
>>> fibonacci(10)
55
'''


from typing import Callable


__version__ = '0.0.1'


def fibonacci(n: int, cls: Callable = int):
    '''
    Calculate the nth Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to calculate.
        cls (type): The class to use for the calculation.

    Returns:
        The nth Fibonacci number.
    '''
    if n < 0:
        return fibonacci(-n, cls) if n & 1 else -fibonacci(-n, cls)
    if n < 2:
        return n
    a, b = cls(0), cls(1)
    for c in bin(n)[3:]:
        s = a**2
        a, b = b**2 + s, (a + b)**2 - s
        if c == '1':
            a, b = b, a + b
        n >>= 1
    return b