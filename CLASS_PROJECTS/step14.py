# step 14 ( Aggregation)

class Person:
    def __init__(self, name):  # Fixed constructor
        self.name = name

class Department:
    def __init__(self, emp):  # Fixed constructor
        self.emp = emp

p = Person("Qasim")
d = Department(p)

print(p.name)
print(d.emp.name)
