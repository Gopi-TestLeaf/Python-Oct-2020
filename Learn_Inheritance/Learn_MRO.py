class A:
    pass

class B:
    def m5(self):
        print("from B")


class C(A, B):
    pass


class D:
    def m5(self):
        print("from D")

class E(C, D):
    pass

x = E()
print(E.__mro__) #Method Resolution Order(MRO)

