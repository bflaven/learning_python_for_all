#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 009_0_class_model_face_python_for_family.py
python3 009_0_class_model_face_python_for_family.py

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

"""[
! Class Face
Hairs
Eyes
Nose
Mouth
Ears
Chin]
    """
print ("\n --- \/ RESULT \n")


# 009_0_class_model_face_python_for_family.py
print("\n --- 009_0_class_model_face_python_for_family.py \n")


class Face():
    """A simple attempt to model a face."""

    def __init__(self, genre, age):
        """Initialize genre and age attributes."""
        self.genre = genre
        self.age = age

    def hairs (self, color):
        """Simulate a single color."""
        self.color = color
        print("My suspect is a "+self.genre.title()+" and has "+self.color+" hairs.")

    def eyes(self, color):
        """Simulate rolling over in response to a command."""
        self.color = color
        print("My suspect is a "+self.genre.title()+" and has "+self.color+" eyes.")


first_face = Face('man', 50)
second_face = Face('child', 11)
# example_1
print("My suspect is a " + first_face.genre.title() + ".")
print("My suspect is " + str(first_face.age) + " years old.")
first_face.hairs("black")
first_face.eyes("blue")

print("\n\n")

# example_2
print("My suspect is a " + second_face.genre.title() + ".")
print("My suspect is " + str(second_face.age) + " years old.")
second_face.hairs("red")
second_face.eyes("green")

print ("\n --- /\ RESULT \n")




