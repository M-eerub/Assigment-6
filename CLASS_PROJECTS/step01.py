# Step 1 (Using self student class)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print("name:", self.name)
        print("grade:", self.grade)

s1 = Student("Aqsa", 75)
s1.display()   # ← Yeh line add karein
