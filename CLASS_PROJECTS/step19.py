# step 19 (callable() and call())

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor


m = Multiplier(5)
print(callable(m))  # True, because __call__ is defined
print(m(3))         # Outputs 15
