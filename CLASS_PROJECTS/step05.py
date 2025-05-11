# step 5 (Static methods-Math class)

class Math:
    @staticmethod
    def add(a, b):
        return a + b

# Call the static method outside the class
result = Math.add(10, 20)
print("sum:", result)
