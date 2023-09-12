import numpy as np
from interpolation import Interpolation
from math import sqrt
from math import log
from math import exp
from sys import maxsize

class Cubic(Interpolation):
    def __init__(self, x1, x2, f, df, tolerance, iterations):
        super().__init__(x1, -maxsize, x2, f, tolerance, iterations)
        self.df = df
        
    def interpolation_optimization(self):
        xmin = 0
        cnt = 0
        
        for _ in range(self.iterations):
            f1 = self.f(self.x1)
            f2 = self.f(self.x2)
            df1 = self.df(self.x1)
            df2 = self.df(self.x2)
                        
            a = 3 * (f2 - f1)
            delta = self.x2 - self.x1
            b = df1 * df2 * delta ** 2
            
            s = (a - df1 * delta - df2 * delta) ** 2 - b
            q = sqrt(s) + a - (df2 + 2 * df1) * delta
            p = df1 * delta ** 2
            
            xmin = self.x1 - p / q
                        
            if abs(xmin - self.x1) < self.tolerance:
                break
                        
            if self.df(xmin) > 0:
                self.x2 = xmin
            else:
                self.x1 = xmin
            
            cnt += 1
            
        print(cnt)
        
        return xmin
    
f = lambda x: x * exp(x)

df = lambda x: (x + 1) * exp(x)

solver = Cubic(0, 1, f, df, 0.01, 1000)

print(solver.interpolation_optimization())