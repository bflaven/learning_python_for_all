#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 006f_python_for_family.py
python3 006f_python_for_family.py

Source: TP_5
Extract from chap_06 python_crash_course


"""

print ("\n --- \/ RESULT \n")


# many_users.py
print("\n --- many_users.py \n")

users = {
    'aeinstein': {'first': 'albert',
                  'last': 'einstein',
                  'location': 'princeton'},
    'mcurie': {'first': 'marie',
               'last': 'curie',
               'location': 'paris'},
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    
    

print ("\n --- /\ RESULT \n")




