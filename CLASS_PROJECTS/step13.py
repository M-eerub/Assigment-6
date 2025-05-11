# step 13 ( Composition)

class Engine:
    def Start(self):
        return "Engine has been started"

class Car:
    def __init__(self, engine):  # Corrected constructor
        self.engine = engine

    def Final(self):
        return self.engine.Start()

e = Engine()
car = Car(e)
print(car.Final())
