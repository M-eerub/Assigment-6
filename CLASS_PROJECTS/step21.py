# step 21 (Make a Custom Class Iterable)

class Countdown:
    def __init__(self, start):
        self.current = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1
        if self.current < 0:
            raise StopIteration
        return self.current

# Using the class
for num in Countdown(5):
    print(num)
