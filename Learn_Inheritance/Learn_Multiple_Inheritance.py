class A:

    def a(self):
        print("I'm from Class A")

    def b(self):
        print("I'm from Class A")


class B:

    def b(self):
        print("I'm from Class B")


class C(B, A):

    def c(self):
        print("I'm from Class C")

cc = C()
cc.c()
cc.b()