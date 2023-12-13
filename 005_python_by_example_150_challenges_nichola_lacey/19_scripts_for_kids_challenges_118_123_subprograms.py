#!/usr/bin/python
# -*- coding: utf-8 -*-
#


"""
https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md#the-world


python --version
# Python 2.7.10

python3 --version
# Python 3.7.7

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_000_python_for_family/002_learn_code_for_kids/english_booK_python_by_example/

# required
python 19_scripts_for_kids_challenges_118_123_subprograms.py
python3 19_scripts_for_kids_challenges_118_123_subprograms.py


https://github.com/abdo0/python-by-example-150-challenges

"""



def get_names ():
    user_name = input("Enter your name: ")
    return user_name


def print_msg(user_name):
    print("Hello "+user_name+"!")
    
def main ():
    user_name = get_names()
    print_msg(user_name)

if __name__ == "__main__":
    main()

# MODEL

# def ask_for_number():
#     num = int(input("Please, give me a number: "))
#     return num


# def count_number(num):
#     for count in range(1, num + 1):
#         print(count)


# def challenge_118():
#     num = ask_for_number()
#     count_number(num)


# if __name__ == "__main__":
#     challenge_118()
