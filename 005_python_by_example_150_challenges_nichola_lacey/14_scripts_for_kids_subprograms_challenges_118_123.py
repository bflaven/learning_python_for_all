#!/usr/bin/python
# -*- coding: utf-8 -*-
#


"""
https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md#the-world


python --version
# Python 2.7.10

python3 --version
# Python 3.7.7



cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_learn_code_for_kids/python_by_example/

python 14_scripts_for_kids_subprograms_challenges_118_123.py
python3 14_scripts_for_kids_subprograms_challenges_118_123.py

"""

# DEMO
"""
def get_data():
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    data_tuple = (user_name, user_age)
    return data_tuple


def message(user_name, user_age):
    if user_age <= 10:
        print("Hi", user_name)
    else:
        print("Hello", user_name)

def main():
    user_name,user_age = get_data()
    message(user_name,user_age)

# launch the main subprogram
main()

"""


# challenge 118
# def ask_value():
#     num = int(input("Enter a number: "))
#     return num


# def count(num):
#     n=1
#     while n <= int(num):
#         print (n)
#         # n = n+1
        
# def main ():
#     num = ask_value
#     count (num)
    
# main()

# challenge 118 (GOOD)
"""
def ask_for_number():
    num = int(input("Please, give me a number: "))
    return num


def count_number(num):
    for count in range(1, num + 1):
        print(count)


def challenge_118():
    num = ask_for_number()
    count_number(num)

if __name__ == "__main__":
    challenge_118()
"""

"""
# challenge_119()
import random

def pick_number ():
    low = int(input("Enter the bottom of the range: "))
    high = int(input("Enter the top of the range: "))
    comp_num = random.randint(low, high)
    return comp_num

def first_guess():
    print ("I am thinking of a number...")
    guess = int(input("Try again: "))
    return guess
    
    
def check_answer():
    try_again == True
    while try_again == True:
        if comp_num == guess:
            print("You win!")
        elif comp_num > guess:
            print("Too high")
            guess = int(input("Try again: "))
        else:
            print("Too low, try again")
            guess = int(input("Try again: "))



def challenge_119():
    comp_num = pick_number()
    guess = first_guess()
    check_answer(comp_num, guess)
    
    
if __name__ == "__main__":
    challenge_119()
"""
   
   
"""
Define a subprogram that will ask the user to pick a low and a high number,
and then generate a random number between those two values and store it in
a variable called “comp_num”.

Define another subprogram that will give the instruction “I am thinking
of a number…” and then ask the user to guess the number they are thinking of.

Define a third subprogram that will check to see if the comp_num is the same
as the user’s guess. If it is, it should display the message “Correct, you
win”, otherwise it should keep looping, telling the user if they are too low or
too high and asking them to guess again until they guess correctly.
"""


import random
import common_functions
def ask_for_user_numbers():
    num_low = 0
    num_high = 0

    while num_low >= num_high:
        num_low = common_functions.get_user_input_integer(
            "Please, enter the minimum number: "
        )
        num_high = common_functions.get_user_input_integer(
            "Please, enter the maximum number: "
        )

        print(
            "Please ensure that the minimum number is smaller than the maximum number"
        )
    return random.randrange(num_low, num_high)
    print(random.randrange(num_low, num_high))

def prompt_for_guess():
    print("\nI am thinking of a number… ")
    guess = common_functions.get_user_input_integer(
        "Please, enter the number I am thinking of: "
    )
    return guess


def check_user_choice(computer_choice, user_guess):
    while True:
        if computer_choice == user_guess:
            print("Correct, you win!")
            return

        if user_guess > computer_choice:
            user_guess = common_functions.get_user_input_integer(
                "Please, enter a lower number: "
            )
        else:
            user_guess = common_functions.get_user_input_integer(
                "Please, enter a higher number: "
            )


def challenge_119():
    computer_choice = ask_for_user_numbers()
    user_guess = prompt_for_guess()
    check_user_choice(computer_choice, user_guess)


if __name__ == "__main__":
    challenge_119()
