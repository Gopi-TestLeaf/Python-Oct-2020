class A:

    def a(self):
        print("I'm from Class A")


class B(A):

    def b(self):
        print("I'm from Class B")


class C(B):

    def c(self):
        print("I'm from Class C")

cc = C()
cc.c()
cc.b()
cc.a()

