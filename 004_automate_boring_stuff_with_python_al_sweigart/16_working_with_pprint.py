#! python3



"""

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_000_python_for_family/002_learn_code_for_kids/automate_boring_stuff_with_python_al_sweigart

python3 16_working_with_pprint.py

https://automatetheboringstuff.com/#toc



"""


import pprint 
message = 'It was a bright cold day in April, and the clocks were striking thirteen.' 
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    pprint.pprint(count)





