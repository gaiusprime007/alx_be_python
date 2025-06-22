import math
class Shape:
    def area(self):
        return NotImplementedError("Subclasses must implement this method")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
##Overide area method in this class
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius
##override area method in Circle class
    def area(self):
        return math.pi * (self.radius ** 2)
    
