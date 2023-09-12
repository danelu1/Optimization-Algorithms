from math import sqrt
from search import Search

# The number obtained from the golden_ratio - 1
phi = (sqrt(5) - 1) / 2

class GoldenSection(Search):
# Function which finds the solution of an optimization problem(minimization).
# The function calculates the interval difference between "a" and "b"(where we
# want to find a solution) and keeps iterating until the difference is strictly 
# smaller than the given tolerance.
# In each iteration we find the points which are at distance "phi * (b - a)" from
# "a" and "b" and then compare the values of the given function in these two points.
# If "f(alpha) > f(beta)", we eliminate any point greater than "alpha" and so "alpha"
# becomes the new "b". Otherwise, "beta" will become the new "a".
    def search_optimization(self):
        difference = self.b - self.a
        
        while difference >= self.tolerance:
            alpha = self.a + phi * difference
            beta = self.a + (1 - phi) * difference
            
            f_alpha = self.f(alpha)
            f_beta = self.f(beta)
                    
            if f_alpha > f_beta:
                self.b = alpha
            else:
                self.a = beta
                        
            difference = self.b - self.a
                            
        return self.a, self.b