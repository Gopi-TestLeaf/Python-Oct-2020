class TestLeaf:

    ts = 12345
    gopi_office = 2345
    _gopi_pers = 400200         # Data Hidding

    def _eval_Tra(self):
        print("et")

    def python(self):
        print('Python')

    def data_science(self):
        print('DS')

    def docker(self):
        print('Docker')

    def get_data(self):
        return TestLeaf._gopi_pers

    def set_data(self, new_ph):
        TestLeaf._gopi_pers = new_ph


    def get_method(self):
        return TestLeaf._eval_Tra(self)



x = TestLeaf()
# print(x.get_data())
# x.set_data(101010)
# print(x.get_data())
x.get_method()
