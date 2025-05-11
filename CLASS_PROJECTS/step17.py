# step 17 (Class Decorators)

class Person:
  def Greet(self,name):
    self.name = name
    print(f"Hello {self.name} How are you")
p1 = Person()
p1.Greet("Aqsa")