"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Practical_6.car import Car


def main():
    """Demo test code to show how to use car class."""
    limo = Car(100)
    limo.add_fuel(20)
    print("limo_fuel = ", limo.fuel)
    limo.drive(115)
    print("limo_odo = ", limo.odometer)
    print(limo)


    my_car = Car(180)
    my_car.add_fuel(50)
    my_car.drive(100)
    print("my_car_fuel =", my_car.fuel)
    print("my_car_odo =", my_car.odometer)
    print(my_car)

    print("My Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Limo Car {}, {}".format(limo.fuel, limo.odometer))

    print("My Car {self.fuel}, {self.odometer}".format(self=my_car))
    print("Limo Car {self.fuel}, {self.odometer}".format(self=limo))




main()
