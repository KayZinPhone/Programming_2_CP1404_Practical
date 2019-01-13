from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, price_per_km=4.50, fanciness=0.0):
        super().__init__(name,fuel)
        self.fanciness = self.price_per_km*fanciness
        self.price_per_km = price_per_km
        self.flagfall = 4.50

    def get_fare(self):
        pass
    def __str__(self):
        return "{}, fuel={}, odo={}, {}km on current fare, ${}/km plus flagfall of ${}".format(self.name, self.fuel, self.odometer, self.current_fare_distance, self.get_fare(), self.flagfall)



