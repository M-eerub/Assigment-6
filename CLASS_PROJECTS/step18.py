# step 18 (Property Decorators: @property, @setter, and @deleter)

class Products:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        if hasattr(self, "_price"):
            return self._price
        else:
            return "Price has been deleted."

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price


# Example usage
p1 = Products(180)
print(p1.price)     # 180
p1.price = 200
print(p1.price)     # 200
del p1.price
print(p1.price)     # Price has been deleted.
