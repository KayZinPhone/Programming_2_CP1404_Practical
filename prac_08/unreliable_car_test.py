from prac_08.unreliable_car import UnreliableCar


bad_car = UnreliableCar("Dodgy", 100, 9)
good_car = UnreliableCar("Mostly Good", 100, 90)


for i in range(1, 12):
    print("{:20} drove {}km".format(good_car.name, good_car.drive(i)))
    print("{:20} drove {}km".format(bad_car.name, bad_car.drive(i)))

print(good_car)
print(bad_car)
