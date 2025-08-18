# class Point:
#     def reset():
#         self.x = 0
#         self.y = 0
# p = Point()
# Point.reset(p)
# print(p.x, p.y)

    class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print("Engine starts with", self.horsepower, "HP")

class Car:
    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine(horsepower)  # Composition: Car HAS-A Engine

    def start_car(self):
        print(f"{self.model} is starting...")
        self.engine.start()

# Usage
my_car = Car("Tesla Model 3", 250)
my_car.start_car()
