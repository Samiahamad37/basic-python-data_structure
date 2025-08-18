# class Bozo:
#     def __init__(self, value):
#         print("Creating a bozo from", value)
#         self.value = 2 * value  # Fixing spacing for better readability
        
#     def clown(self, x):
#         print('Clowning:', x)
#         print(x * self.value)
#         return x + self.value  # Fixed incorrect attribute reference (self.values -> self.value)
    
# def main():  # Moved outside the class
#     print("Clowning around now")
#     c1 = Bozo(1)
#     c2 = Bozo(2)
#     print(c1.clown(3))
#     print(c2.clown(c1.clown(2)))

# main()

# class Test:
#     @classmethod
#     def greet(cls):
#         return "Hello from class method!"

# print(Test.greet())

class Test:
    def _init_(self, value):
        self.value = value

    def add(self, num):
        self.value += num
        return self

    def display(self):
        print(self.value)
        return self

obj = Test(5)
obj.add(10).display().add(5).display()