class A:

    def a(self):
        print("I'm from Class A")
    

class B(A):

    def b(self):
        print("I'm from Class B")

#
# aa = A()
# aa.a()

bb = B()
bb.b()
bb.a()