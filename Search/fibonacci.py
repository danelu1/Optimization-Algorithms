from math import sqrt
from math import log
import sys
# sys.path.append('/c/Users/Bogdan/Desktop/Optimizare/Search/search')
from search import Search

# Constants used for implementation
phi = (sqrt(5) - 1) / 2
p1 = (sqrt(5) + 1) / 2
p2 = (1 - sqrt(5)) / 2

class Fibonacci(Search):
    
    # Implementation for Fibonacci sequence, using the formula obtained from the
    # recurrence: fib(n + 1) = fib(n) + fib(n - 1)
    @staticmethod
    def fib(n):
        if n < 0:
            return -1
        
        return 1./sqrt(5) * (p1 ** n - p2 ** n)

    # Function used for determination of the number of iterations that must be done
    # the "fibonacci_optimization" function.
    # We know that the number of iterations is the smallest "k" which satisfies:
    # fib(k) >= (b - a) / tolerance. After a few calculations regarding this inequality,
    # we get the value of "phi^k" to be in the range [0, 2 / (c + sqrt(c ** 2 - 4))],
    # the best match for the right side of the interval. From here, we get "k" as the
    # closest integer, bigger than log(2 / (c + sqrt(c ** 2 - 4)))/log(phi).
    @staticmethod
    def threshold(a, b, tolerance):
        c = (b - a) / tolerance * sqrt(5)
        k = 2./(c + sqrt(c ** 2 - 4))
        
        return int(log(k) / log(phi)) + 1

    # Same function as "golden_ratio_optimization", but this time the rate of change is
    # given by the fib(k - j) / fib(k - j + 1), instead of "phi".
    def search_optimization(self):
        difference = self.b - self.a
        j = 0
        k = self.threshold(self.a, self.b, self.tolerance)
        
        while difference >= self.tolerance:
            alpha = self.a + self.fib(k - j) / self.fib(k - j + 1) * difference
            beta = self.a + self.fib(k - j - 1) / self.fib(k - j + 1) * difference
            
            f_alpha = self.f(alpha)
            f_beta = self.f(beta)
            
            if f_alpha > f_beta:
                self.b = alpha
            else:
                self.a = beta
                
            difference = self.b - self.a
            
            j += 1
                    
        return self.a, self.b