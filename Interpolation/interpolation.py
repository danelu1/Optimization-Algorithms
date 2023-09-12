# Class implemented for describing what we need for a polynomial interpolation problem
class Interpolation:
    def __init__(self, x1, x2, x3, f, tolerance, iterations):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.f = f
        self.tolerance = tolerance
        self.iterations = iterations
    
    # Function used to do the optimization technique
    def interpolation_optimization(self):
        pass