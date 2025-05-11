# step 7 (Access Modifiers: Public, Private, and Protected)

class Employee:
  def __init__(self):
    self.name="Qasim"
    self._salary=50,000
    self.__pin="727462772"

emp = Employee()
print("Public.name:",emp.name)
print("Protected Salary:", emp._salary)
try:
    print("Private PIN:",emp.__pin)

except AttributeError:
    print("Private PIN: cannot access directly")
print("Accessing private using name mangling:",emp._Employee__pin)

