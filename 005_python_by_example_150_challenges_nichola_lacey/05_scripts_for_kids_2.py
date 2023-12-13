#!/usr/bin/python
# -*- coding: utf-8 -*-
#
"""

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_learn_code_for_kids/python_by_example/

python3 05_scripts_for_kids_2.py



"""


# MORE STRING MANIPULATION

# challenge 81
"""
subject = input("Enter your favourire school subject: ")
for letter in subject:
    print (letter, end="-")
print ("\n")
"""

# challenge 82
def trim_characters(poem, start, end):
    length_poem = len(poem)

    if length_poem < start:
        raise IndexError("list index out of range")

    if isinstance(start, int) and isinstance(end, int):
        if start > 0 and end >= start:
            user_line_choose = poem[start:end]
            return user_line_choose
        else:
            raise IndexError("Input indexes are out of range")
    else:
        raise TypeError("Input indexes are not numeric")
    
def display_line():
    poem = "Oh, I wish I'd looked after me teeth,"
    start = int(input("Enter a starting number: "))
    end = int(input("Enter an ending number: "))

    trimmed_poem = trim_characters(poem, start, end)

    print(trimmed_poem)


if __name__ == "__main__":
    display_line()
    
    

"""
def processing(subject):
    letters = list(subject)
    joined_subject = f"{'-'.join(letters)}-"

    return joined_subject


def favourite_subject():
    subject = input("Enter your favourire school subject: ")
    result = processing(subject)
    print(result)


if __name__ == "__main__":
    favourite_subject()
"""
