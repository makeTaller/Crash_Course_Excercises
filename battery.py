class Battery():
    """ A simpe attermpt to model a battery for an eletric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range theis battery  provides."""
        if self.battery_size ==70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size <= 70:
            self.battery_size = 85
            print("You upgraded your battery!")

