# Class which contains the prerequisites for the "Golden Section" and "Fibonacci"
# optimization problems. The name "Search" comes from the fact that both algorithms
# are for "searching" the range where our minimum lies.
class Search:
    def __init__(self, a, b, f, tolerance):
        self.a = a
        self.b = b
        self.f = f
        self.tolerance = tolerance
        
    def search_optimization(self):
        pass