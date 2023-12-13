#! python3



"""

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_000_python_for_family/002_learn_code_for_kids/automate_boring_stuff_with_python_al_sweigart

python3 14_working_dictionaries_birthdays.py

https://automatetheboringstuff.com/#toc



"""


birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
    else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')

