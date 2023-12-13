#! python3
# lucky.py - Opens several Google search results.

"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/004_automate_boring_stuff_with_python_al_sweigart/


python3 07_swordfish.py


"""

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
