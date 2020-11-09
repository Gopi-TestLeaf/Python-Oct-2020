class TestLeaf:

    def python(self):                               # Instance method
        print('for Dev and DS')

    @classmethod                                    # Class Method
    def email_to_emp(cls):
        print(TestLeaf.v)
        print("emp")

    @staticmethod
    def conf_python():                              # static Method
        print(TestLeaf.v)




per1 = TestLeaf()
per1.python()
#**********************************************************

per1.email_to_emp()
TestLeaf.email_to_emp()


per1.conf_python()
TestLeaf.conf_python()
