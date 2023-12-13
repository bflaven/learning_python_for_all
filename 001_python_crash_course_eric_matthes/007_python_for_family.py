#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 007_python_for_family.py
python3 007_python_for_family.py

Source: TP_8


"""

"""
cities.py
confirmed_users.py
counting.py
even_or_odd.py
greeter.py
mountain_poll.py
parrot.py
pets.py
rollercoaster.py

"""

print ("\n --- \/ RESULT \n")

# parrot.py
print("\n --- parrot.py \n")
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
        
        

# cities.py
print("\n --- cities.py \n")

prompt = "\nPlease tell me a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")



# confirmed_users.py
print("\n --- confirmed_users.py \n")

# Start out with some users that need to be verified,
#  and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user, until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())



# counting.py
print("\n --- counting.py \n")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1



# even_or_odd.py
print("\n --- even_or_odd.py \n")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
# odd :: impair
# even :: pair

# greeter.py
print("\n --- greeter.py \n")
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")


# mountain_poll.py
print("\n --- mountain_poll.py \n")
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # Store the response in the dictionary:
    responses[name] = response
    
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")



# pets.py
print("\n --- pets.py \n")
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


# rollercoaster.py
print("\n --- rollercoaster.py \n")
height = input("How tall are you, in inches? e.g 42 ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")


print ("\n --- /\ RESULT \n")




