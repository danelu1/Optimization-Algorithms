from interpolation import Interpolation

# Class which inherits the previous class and contains an implementation of the
# interpolation_optimization() function
class Quadratic(Interpolation):
    def interpolation_optimization(self):
        a = 0
        b = 0
        xmin = 0
        cnt = 0
        
        # We are iterating as long as "abs(xmin - self.x2) < self.tolerance" or the given
        # number of iterations is reached
        for _ in range(self.iterations):
            
            # Values of the objective function in the given points
            f1 = self.f(self.x1)
            f2 = self.f(self.x2)
            f3 = self.f(self.x3)
            
            # Coefficients of the second order polynomial which we use to approximate the function
            a = - ((self.x2 - self.x3) * f1 + (self.x3 - self.x1) * f2 + (self.x1 - self.x2) * f3) / ((self.x1 - self.x2) * (self.x3 - self.x1) * (self.x1 - self.x2))
            b = (f1 - f2) / (self.x1 - self.x2) - a * (self.x1 + self.x2)
            
            # The minimum of the curve(which is a parabola)
            xmin = (- b) / (2 * a)
            
            if (abs(xmin - self.x2) < self.tolerance):
                break
            
            # For calculating the new interval limits we distinguish two cases:
            #   - "xmin" is less than "x2":
            #       -> f(xmin) is less than f(x2), which means that "xmin" must be inside
            #          the interval [x1, x2]; 
            #       -> f(xmin) is greater than f(x2), which means that f(x2) is closer to
            #          the actual local minimum of the function, so the interval becomes
            #          [xmin, x3];
            #   - "xmin" is greater than "x2" and is followed the same analogy as in the
            #      previous case.
            if xmin < self.x2:
                if self.f(xmin) < f2:
                    self.x3 = self.x2
                    self.x2 = xmin
                else:
                    self.x1 = xmin
            else:
                if self.f(xmin) < f2:
                    self.x1 = self.x2
                    self.x2 = xmin
                else:
                    self.x3 = xmin
                
            # Counter to see how many iterations are done until the convergence of the method
            cnt += 1
                            
        return xmin, cnt