import numpy as np
from conjugate_direction import ConjugateDirections

# User input
n = int(input())

Q = np.array([[0] * n] * n)

for i in range(n):
    for j in range(n):
        Q[i, j] = float(input())

directions = np.array([[0] * n] * n)

for i in range(n):
    for j in range(n):
        directions[i, j] = float(input())

b = np.array([0] * n)

for i in range(n):
    b[i] = float(input())

x = np.array([0] * n)

for i in range(n):
    x[i] = float(input())

solver = ConjugateDirections(x, Q, b, 0.0001, 1000, directions)

print(solver.gradient_optimization())