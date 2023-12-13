#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 009_2_class_car_python_for_family.py
python3 009_2_class_car_python_for_family.py

Source: TP_9


"""

"""
car.py
dog.py
electric_car.py
favorite_languages.py
my_car.py
my_cars.py



"""


print ("\n --- \/ RESULT \n")

# car.py
"""A class that can be used to represent a car."""
# odometer :: cuentakilómetros


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


# output
my_new_car = Car('audi', 'a4', 2015)
print(my_new_car.get_descriptive_name())



print ("\n --- /\ RESULT \n")




