class A:

    a = 100
    b = 200

    def __init__(self, x):
        self.a = x
        print(self.a)


c = A(000)
print(A.a)
