from prac_08.taxi import Taxi

# taxi = Taxi("Prius 1", 100, 1.23)
# taxi.drive(40)
# print(taxi)
# print("Current fares: ", taxi.get_fare())
#
# taxi.start_fare()
# taxi.drive(100)
# print(taxi)
# print("Current fares second: ", taxi.get_fare())

taxi = Taxi("Prius 1",100)
taxi.drive(120)
print(taxi)
print("Current fare", taxi.get_fare())