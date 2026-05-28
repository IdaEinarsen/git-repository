# 9.9 Battery Upgrade

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""

        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size < 65:
            self.battery_size = 65


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery = Battery()


# Create an electric car
my_leaf = ElectricCar("nissan", "leaf", 2024)

print(my_leaf.get_descriptive_name())

# Show original range
my_leaf.battery.get_range()

# Upgrade the battery
my_leaf.battery.upgrade_battery()

# Show upgraded range
my_leaf.battery.get_range()








