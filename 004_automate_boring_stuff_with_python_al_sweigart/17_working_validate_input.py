#! python3



"""

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_000_python_for_family/002_learn_code_for_kids/automate_boring_stuff_with_python_al_sweigart

python3 17_working_validate_input.py


https://automatetheboringstuff.com/#toc



"""


while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
while True:
        print('Select a new password (letters and numbers only):')
        password = input()
        if password.isalnum():
            break
        print('Passwords can only have letters and numbers.')
        
        
        







