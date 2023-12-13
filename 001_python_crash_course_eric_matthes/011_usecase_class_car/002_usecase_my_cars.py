#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/002_learning_python_for_family/001_python_for_family/011_usecase_class_car/

python 002_usecase_my_cars.py


"""

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2015)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2015)
print(my_tesla.get_descriptive_name())


