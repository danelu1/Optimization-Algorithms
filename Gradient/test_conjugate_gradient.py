import numpy as np
from conjugate_gradient import ConjugateGradient

# User input
n = int(input())

Q = np.array([[0] * n] * n)

for i in range(n):
    for j in range(n):
        Q[i, j] = float(input())

b = np.array([0] * n)

for i in range(n):
    b[i] = float(input())

x = np.array([0] * n)

for i in range(n):
    x[i] = float(input())

solver = ConjugateGradient(x, Q, b, 0.000001, 1000)

xmin = solver.gradient_optimization()

print(f'xmin: {xmin}')

f = lambda x: 1 / 2 * np.dot(np.dot(x.T, Q), x) - np.dot(x.T, b)

print(f'f(xmin) = {f(xmin)}')