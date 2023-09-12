from fibonacci import Fibonacci
from math import exp
from math import log

# Example function for testing
f = lambda x: x * exp(x ** 2) + x * log(x)

# User input
x = float(input())
y = float(input())
tolerance = float(input())

# Result
solver = Fibonacci(x, y, f, tolerance)
a, b = solver.search_optimization()

print(f'The solution is in the interval: [{a}, {b}]')