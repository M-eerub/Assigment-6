# step 3 (Public variables and methods-car class)

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} Car is starting.....")

my_Car = Car("Toyota")
print("Car brand:", my_Car.brand)
my_Car.start()
