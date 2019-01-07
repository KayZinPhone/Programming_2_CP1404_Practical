class Car:
    def __init__(self, name="simple car"):
        self.name = name

class Ferrari(Car):
    def __init__(self, name="Rd Ferrari", mph=80):
        super().__init__(name)
        self.mph = 80

C1 = Car("Red Car")
C2 = Ferrari()
C3 = C1



print("C1 object", C1.name)
print("C2 object", C2.name)
print("C3 object", C3.name)