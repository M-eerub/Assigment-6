# step 10 (Instance Methods)

class Dog:
  def __init__(self,name,breed):
    self.name = name
    self.breed = breed

  def bark(self):
    print(f"{self.name}Says: Woof! Woof!")

dog1 = Dog("Tommy","buddy")
dog1.bark()