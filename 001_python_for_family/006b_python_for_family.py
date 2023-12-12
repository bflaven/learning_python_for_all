#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/001_python_for_family/

python 006b_python_for_family.py
python3 006b_python_for_family.py

Source: TP_5
Extract from chap_06 python_crash_course


"""

print ("\n --- \/ RESULT \n")

# require python3
# favorite_languages.py
print("\n --- favorite_languages.py \n")

favorite_languages = {
    'louise': 'spanish',
    'arthur': 'portuguese',
    'bruno': 'russian',
    'anne': 'english',
}

# example_1
# language = favorite_languages['bruno'].title()
# print(f"Bruno's favorite language is {language}.")



# example_2
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#           language.title() + ".")

# example_3
# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)


# example_4
# user.py
# print("\n --- user.py \n")

# user_0 = {
#           'username': 'efermi',
#           'first': 'enrico',
#           'last': 'fermi',
#           }

# kid = {
#     'firstname':'Louise',
#     'lastname':'Flaven',
#     'age': '13',
# }


# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)

# for k, v in kid.items():
#     print("\nKey: " + k)
#     print("Value: " + v)

# example_5
favorite_languages = {
    'louise': 'spanish',
    'arthur': 'portuguese',
    'bruno': 'russian',
    'anne': 'english',
}
# for language in favorite_languages.values():
for name in favorite_languages.keys():
    
    # print(language.title())
    print(name.title())



print ("\n --- /\ RESULT \n")




