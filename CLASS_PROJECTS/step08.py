# step 8 (The super() Function)

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show(self):
        print(f"name: {self.name}, subject: {self.subject}")

t1 = Teacher("Mr. Muneeb", "Python")
t1.show()

