class Car:

    def sound_horn(self):
        print("sound horn")

    def apply_brake(self):
        print("brake")


class BMW(Car):

    def apply_brake(self):
        print("ABS Brake")


class Audi(Car):
    pass


b= BMW()
b.apply_brake()

a = Audi()
a.apply_brake()

