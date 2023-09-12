import matplotlib.pyplot as plt
import numpy as np
from math import log
from math import exp
from quadratic_interpolation import Quadratic

# Test function
f = lambda x: x + 3 * log((x + 3) / (x - 1))

# User input
x1 = float(input())
x2 = float(input())
x3 = float(input())
tolerance = float(input())
iters = int(input())

# Example: Quadratic(0.01, 3, 10, f, 0.00001, 1000)
solver = Quadratic(x1, x2, x3, f, tolerance, iters)

xmin, iters = solver.interpolation_optimization()

# Values generated between 1.01 and 10 for the function
x = np.linspace(1.01, 10, 10000)

# Array where we compute "f(x)"
y = np.array([0] * len(x))

for i in range(len(y)):
    y[i] = f(x[i])

x_min = "{:.4f}".format(xmin)
y_min = "{:.4f}".format(f(xmin))

# Graph of the function with minimum point on the given interval
plt.plot(x, y, label = 'y = f(x)')
plt.title('Graph of y = f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(xmin, f(xmin), marker = 'x', color = 'red', label = '(xmin, f(xmin))')
plt.annotate(f'({x_min}, {y_min})', (xmin, f(xmin)), textcoords ="offset points")
plt.show()

print(f'Minimum value of the function in the specified range: {solver.f(xmin)}')
print(f'Value for which the minimum is reached: {xmin}')
print(f'Number of iterations for reaching the tolerance: {iters}')