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


if __name__ == '__main__':
    from sympy import fibonacci as sympy_fibonacci
    from random import randrange
    from decimal import Decimal, localcontext, MAX_PREC, MIN_EMIN, MAX_EMAX
    from asyncio import timeout, run
    from time import time
    from functools import wraps
    from modulo import mod

    class Test:
        n = 0
        tests = []

        def __init__(self, name: str = '', timeout: float = 5.0):
            Test.n += 1
            self.name, self.timeout, self.id = name, timeout, Test.n

        def __str__(self):
            return f'Test({self.name}, {self.timeout})'
        
        def __call__(self, test: Callable):
            @wraps(test)
            async def wrapper(*args, **kwargs):
                print(end=f"Test {self.id}{f' ({self.name})' if self.name else ''}: ")
                start = time()
                try:
                    async with timeout(self.timeout):
                        await test(*args, **kwargs)
                    print(f'Passed in {time() - start:.3f}s')
                    return True
                except Exception as e:
                    print(f"Failed in {time() - start:.3f}s ({e.__class__.__name__}{f': {e}' if str(e) else ''})")
                    return False
            Test.tests.append(wrapper)
            return wrapper
        
        @classmethod
        async def run(cls):
            count = 0
            for test in cls.tests:
                count += await test()
            print(f'{count}/{len(cls.tests)} tests passed')
            return count

    @Test('tiny')
    async def test_tiny():
        for i in range(12):
            assert fibonacci(i) == sympy_fibonacci(i)

    @Test('small')
    async def test_small():
        for i in range(12, 144):
            assert fibonacci(i) == sympy_fibonacci(i)
    
    @Test('medium')
    async def test_medium():
        for i in range(144, 1728):
            assert fibonacci(i) == sympy_fibonacci(i)
    
    @Test('large')
    async def test_large():
        for _ in range(12):
            n = randrange(1728, 248832)
            assert fibonacci(n) == sympy_fibonacci(n)
    
    @Test('huge')
    async def test_huge():
        n = randrange(248832, 2985984)
        assert fibonacci(n) == sympy_fibonacci(n)
    
    @Test('negative')
    async def test_negative():
        for i in range(-12, 0):
            assert fibonacci(i) == sympy_fibonacci(i)
    
    @Test('decimal')
    async def test_decimal():
        with localcontext(prec=MAX_PREC, Emin=MIN_EMIN, Emax=MAX_EMAX):
            assert fibonacci(248832, Decimal) == sympy_fibonacci(248832)
    
    @Test('large_decimal')
    async def time_large_decimal():
        with localcontext(prec=MAX_PREC, Emin=MIN_EMIN, Emax=MAX_EMAX):
            fibonacci(2985984, Decimal)
    
    @Test('modulo')
    async def test_modulo():
        assert fibonacci(79496847203390844133441536, lambda n: mod(n, 998244353)) == mod(357977786, 998244353)

    run(Test.run())