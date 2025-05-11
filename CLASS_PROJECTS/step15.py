# step 15 (Method Resolution Order (MRO) and Diamond Inheritance)

class A:
    def Show(self):
        print("A")

class B(A):
    def Show(self):
        print("B")

class C(A):
    def Show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.Show()
