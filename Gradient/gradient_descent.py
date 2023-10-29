import numpy as np
from math import sqrt
from gradient import Gradient

class GradientDescent(Gradient):
    
    # Method which describes the "steepest descent" algorithm. The gradient is computed initially
    # as "Q * x - b"(this can be proven by doing the derivative of the objective function "f"
    # after the direction "x"). For each step we compute the "alpha" parameter which represents
    # the descent of the function for the current iteration. The "is_positive" variable checks if
    # there exists a moment during the algorithm when the "x.T * Q * x" is not positive. We stop
    # the iterations in case that the gradient in the chosen point is almost zero(the necessary
    # condition to prove the point is stationary).
    def gradient_optimization(self):
        g = np.dot(self.Q, self.x) - self.b
        cnt = 0
        is_positive = True
        
        for _ in range(self.iterations):
            if np.dot(np.dot(self.x.T, self.Q), self.x) < 0:
                self.Q = -self.Q
                is_positive = False
            
            alpha = np.dot(g.T, g) / np.dot(np.dot(g.T, self.Q), g)
            self.x = np.subtract(self.x, alpha * g)
            g = np.dot(self.Q, self.x) - self.b
            cnt += 1
            
            if np.linalg.norm(g, ord = 2) < self.tolerance:
                break
            
        return self.x, cnt, is_positive