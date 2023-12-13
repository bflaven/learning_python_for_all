#! python3



"""

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_000_python_for_family/002_learn_code_for_kids/automate_boring_stuff_with_python_al_sweigart

python3 15_working_dictionaries_keys_values_items.py

https://automatetheboringstuff.com/#toc



"""

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)
# red
# 42


for k in spam.keys():
    print(k)
# color
# age

for i in spam.items():
    print(i)
# ('color', 'red')
# ('age', 42)

# spam.keys()
# dict_keys(['color', 'age'])
# list(spam.keys())
# ['color', 'age']

for k, v in spam.items(): 
    print('Key: ' + k + ' Value: ' + str(v))
# Key: age Value: 42
# Key: color Value: red
