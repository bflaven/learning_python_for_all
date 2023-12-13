#! python3


"""

cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/004_automate_boring_stuff_with_python_al_sweigart/



python3 02_hello.py



https://automatetheboringstuff.com/#toc



"""


# This program says hello and asks for my name.

print('Hello world!')
print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
