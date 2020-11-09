class A:

    ls = []
    def __init__(self, *args):
        self.ls = args
        print(self.ls)



x = A('a', 'b', 'c')         # OverLoading
y = A(1,2)                   # OverLoading

