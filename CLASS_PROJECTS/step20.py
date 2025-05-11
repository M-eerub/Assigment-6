# step 20 (Creating a Custom Exception)

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    print("Access Granted")  # This should be inside the function

try:
    check_age(17)
except InvalidAgeError as e:
    print(e)
