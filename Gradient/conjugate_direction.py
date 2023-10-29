import numpy as np
from gradient import Gradient

# Class used to describe the "conjugate directions" optimization method.
class ConjugateDirections(Gradient):
    def __init__(self, x, Q, b, tolerance, iterations, directions):
        super().__init__(x, Q, b, tolerance, iterations)
        self.directions = directions
        
    # Function used to implement the "conjugate directions" algorithm.
    # The function computes the directions using the above function and
    # uses them to compute the minimum of our expression.
    def gradient_optimization(self):
        g = np.dot(self.Q, self.x) - self.b
        
        for i in range(len(self.directions)):
            alpha = - np.dot(g.T, self.directions[:, i]) / np.dot(np.dot(self.directions[:, i].T, self.Q), self.directions[:, i])
            self.x = self.x + alpha * self.directions[:, i]
            g = np.dot(self.Q, self.x) - self.b
            
            print(alpha)
            
            print(self.x)
            
            print(g)
            
        return self.x