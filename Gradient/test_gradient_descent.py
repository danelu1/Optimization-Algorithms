import numpy as np
from gradient_descent import GradientDescent

# User input 
n = int(input())

Q = np.array([[0] * n] * n)

for i in range(len(Q)):
    for j in range(len(Q[0])):
        Q[i, j] = float(input())

b = np.array([0] * n)

for i in range(len(b)):
    b[i] = float(input())

x = np.array([0] * n)

tolerance = float(input())

iters = int(input())

# Solver for the "steepest descent" method
solver = GradientDescent(x, Q, b, tolerance, iters)

xmin, cnt, is_positive = solver.gradient_optimization()

# Test function
f = lambda x : 1 / 2 * np.dot(np.dot(x.T, Q), x) - np.dot(x.T, b)


if is_positive:
    print(f'Point where the minimum is reached: {xmin}')
    print(f'Minimum value of the function: {f(xmin)}')
else:
    print(f'Point where the maximum is reached: {xmin}')
    print(f'Maximum value of the function: {f(xmin)}')
    
print(f'Number of iterations to reach the value: {cnt}')