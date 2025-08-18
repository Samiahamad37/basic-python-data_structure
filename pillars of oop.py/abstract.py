# hiding the implementation details of a class while exposing only the essential features

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        print("Calculating area of Rectangle")
