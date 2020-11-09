class Mobile:

    def __init__(self, name, ph_no):
        self.name = name
        self.ph_no= ph_no

    def dial_number(self):
        print(self.name)
        print(self.ph_no)
        print('dialing')

    def send_sms(self, msg):
        print(self.name)
        print(self.ph_no)
        print(msg)
        print('sending')


class A:
    pass
# *****************************************************************
obj1 = Mobile('Divya', '12345')
obj1.dial_number()
obj1.send_sms('hi')

#obj2 = Mobile('Gopi', 65432)

