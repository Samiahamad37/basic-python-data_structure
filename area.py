# calculating rectangle
class Rectangle:
    def __init__(self ,length,width):
        self.a=length
        self.b=width
obj=Rectangle(20,10)
print("Area of a rectangle is", obj.a*obj.b)
print("peremeter of rectangle is" ,obj.a+obj.b)    

  
  
#   calculating triangle
h=float(input("enter height: "))
b=float(input("enter base: "))
a=1/2*(h*b)
print(a,"Area of triangle")


# determining the cycle of the object
class Cycle:
    def __init__(self,side):
        self.x=side
obj=Cycle(5)
print((obj.x)**2)
        
        
        # calculating cycle
import math
x=float(input("Enter radius: "))
y= math.pi*(x**2)
print(y,"is area of circle")
        