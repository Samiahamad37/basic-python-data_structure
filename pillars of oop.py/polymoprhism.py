# is the ability of diffrent  object to respond to the same method call in different 

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Calculating area of Circle")

class Square(Shape):
    def area(self):
        print("Calculating area of Square")
