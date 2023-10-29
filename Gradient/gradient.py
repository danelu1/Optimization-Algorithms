# Class used to describe the characteristics of any "Gradient" optimization algorithm
# for any function with the form: f(x) = 1/2 * x.T * Q * x - x.T * b, where "Q" is a
# positive defined matrix.
class Gradient:
    def __init__(self, x, Q, b, tolerance, iterations):
        self.x = x
        self.Q = Q
        self.b = b
        self.tolerance = tolerance
        self.iterations = iterations
        
    def gradient_optimization(self, f):
        pass