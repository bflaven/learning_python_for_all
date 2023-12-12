#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/002_learning_python_for_family/001_python_for_family/011_usecase_class_car/

python 001_usecase_my_car.py

"""

from car import car

my_new_car = Car('audi', 'a4', 2015)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
