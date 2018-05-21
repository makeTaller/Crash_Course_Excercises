"""A class that can be used to represent a car."""
class Car():
    """A simple attempt to represent a car."""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading  = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading =mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self,make,model,year):
        """ Initialize attributes of the parent class."""
        super().__init__(make,model,year)
        self.battery = Battery()


my_car = ElectricCar('tesla', 'model s', 2016)
print(my_car.get_descriptive_name())
my_car.battery.describe_battery()
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()
my_car.battery.describe_battery()
