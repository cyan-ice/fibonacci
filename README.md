# Fibonacci - A Python Library for Fibonacci Numbers

This library provides a simple interface for calculating Fibonacci numbers.
It supports both small and large numbers, and provides a variety of
options for customization.

## Installation

### From Source

You can clone the repository and install the package locally:

#### Unix/macOS

```bash
git clone https://github.com/cyan-ice/fibonacci
cd fibonacci
python3 -m pip install .
```

#### Windows

```bash
git clone https://github.com/cyan-ice/fibonacci
cd fibonacci
py -m pip install .
```

### From Wheel

Or you can download the wheel file from the [releases](https://github.com/cyan-ice/fibonacci/releases) or the [dist directory](https://github.com/cyan-ice/fibonacci/tree/main/dist) and install it:

#### Unix/macOS

```bash
python3 -m pip install fibonacci-<version>-py3-none-any.whl
```

#### Windows

```bash
py -m pip install fibonacci-<version>-py3-none-any.whl
```

## Usage

```python
>>> from fibonacci import fibonacci
>>> fibonacci(10)
55
```

## Test

### Unix/macOS

```bash
python3 -m pip install sympy modulo
python3 -m fibonacci
```

### Windows

```bash
py -m pip install sympy modulo
py -m fibonacci
```

You should see something like this:

```plain
Test 1 (tiny): Passed in 0.000s
Test 2 (small): Passed in 0.000s
Test 3 (medium): Passed in 0.035s
Test 4 (large): Passed in 0.132s
Test 5 (huge): Passed in 0.281s
Test 6 (negative): Passed in 0.003s
Test 7 (decimal): Passed in 0.263s
Test 8 (large_decimal): Passed in 0.201s
Test 9 (modulo): Passed in 0.000s
9/9 tests passed
```
