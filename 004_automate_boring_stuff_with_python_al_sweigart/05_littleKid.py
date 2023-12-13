#! python3
"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/004_automate_boring_stuff_with_python_al_sweigart/


python 05_littleKid.py


"""

print('\n--- Hello Little Kid! --- ')

print('What is your name?')  # ask for their name
name = input()

print('What is your age?')  # ask for their name
age = input()

if name == 'Louise':
    print('Hi, Louise.')
elif age < 12:
    print('You are not Louise, kiddo.')
else:
    print('You are neither Louise nor a little kid.')
