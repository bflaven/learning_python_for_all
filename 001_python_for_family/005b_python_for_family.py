#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 005_python_for_family.py
python3 005_python_for_family.py

Source: TP_4
Extract from chap_05 python_crash_course

"""





print ("\n --- \/ RESULT \n")



cars = ['audi', 'bmw', 'subaru', 'toyota']

print ("\n --- case_1 \n")
# case_1
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print ("\n --- case_2 \n")
# case_2
for car in cars:
    if car.lower() == 'audi':
        print("True")
        print (car)
    else:
        print("False")
        
        


print ("\n --- /\ RESULT \n")




