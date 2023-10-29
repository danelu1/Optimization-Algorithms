import numpy as np
from gradient import Gradient

class ConjugateGradient(Gradient):
    def gradient_optimization(self):
        dirs = np.array([[float(0)] * len(self.Q)] * len(self.Q))
        
        print(f'Iteration 0')
        
        g = np.dot(self.Q, self.x) - self.b
        
        print(f'g0 = Q * x0 - b = {g}\n')
        
        dirs[:, 0] = - g
        
        print(f'd0 = -g0 = {- g}\n\n')
        
        alpha = 0
        
        n = len(self.Q)
        
        for i in range(1, n):
            print(f'Iteration {i}')
            
            alpha = - np.dot(g.T, dirs[:, i - 1]) / np.dot(np.dot(dirs[:, i - 1].T, self.Q), dirs[:, i - 1])
            
            print(f'alpha{i - 1} = -g{i - 1}(T) * d{i - 1} / d{i - 1}(T) * Q * d{i - 1} = {alpha}\n')
            
            self.x = self.x + alpha * dirs[:, i - 1]
            
            print(f'x{i} = x{i - 1} + alpha{i - 1} * d{i - 1} = {self.x}\n')
            
            g = np.dot(self.Q, self.x) - self.b
            
            print(f'g{i} = Q * x{i} - b = {g}\n')
            
            beta = float(np.dot(np.dot(g.T, self.Q), dirs[:, i - 1])) / np.dot(np.dot(dirs[:, i - 1], self.Q), dirs[:, i - 1])
            
            print(f'beta{i - 1} = g{i}(T) * Q * d{i - 1} / d{i - 1} * Q * d{i - 1} = {beta}\n')
            
            dirs[:, i] = - g + beta * dirs[:, i - 1]
            
            print(f'd{i} = -g{i} + beta{i - 1} * d{i - 1} = {dirs[:, i]}\n')
            
            print('\n\n')
            
        print(f'Iteration {n}: ')
        
        alpha = - np.dot(g.T, dirs[:, n - 1]) / np.dot(np.dot(dirs[:, n - 1].T, self.Q), dirs[:, n - 1])
        
        print(f'alpha{n - 1} = -g{n - 1}(T) * d{n - 1} / d{n - 1}(T) * Q * d{n - 1} = {alpha}\n')
        
        self.x = self.x + alpha * dirs[:, n - 1]
        
        return self.x