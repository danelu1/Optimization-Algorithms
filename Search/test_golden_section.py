from golden_section import GoldenSection
from math import log
from math import exp

# Test function
f = lambda x: x * exp(x ** 2) + x * log(x)
    
# The interval limits and tolerance, read by the user.
x = float(input())
y = float(input())
tolerance = float(input())

solver = GoldenSection(x, y, f, tolerance)
a, b = solver.search_optimization()

# The interval where the function find its minimum value.
print(f'The solution is in the interval: [{a}, {b}]')