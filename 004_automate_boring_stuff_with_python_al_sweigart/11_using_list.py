#! python3


"""

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_000_python_for_family/002_learn_code_for_kids/automate_boring_stuff_with_python_al_sweigart

python3 11_using_list.py

https://automatetheboringstuff.com/#toc



"""

# example_1
# >>> ['Bruno', 'Arthur', 'Anne', 'Louise']
# ['Bruno', 'Arthur', 'Anne', 'Louise']

# example_1a
# >>> ['Bruno', 'Arthur', 'Anne', 'Louise'][0]
# 'Bruno'

# example_2
family = ['Bruno', 'Arthur', 'Anne', 'Louise']
# print(family)

# example_3
# print(family[0])
# print(family[1])
# print(family[2])
# print(family[3])

# family[0]
# family[1]
# family[2]
# family[3]

# example_4
# print('Hello ' + family[2])

# example_5 (ERROR)
# print('Hello ' + family[500])

# example_6 (ERROR)
# >>> spam = ['cat', 'bat', 'rat', 'elephant']
# >>> spam[1]
# 'bat'

# example_7
# >>> spam[1.0]
# >>> spam[int(1.0)]
# 'bat'

# example_8 (ERROR)
# print('Hello ' + family[2.0])

# example_8 (ERROR)
# print('Hello ' + family[int(0.0)])


# example_9 
# family[-1]
# family[-2]
# family[-3]
# print('Hello ' + family[-1])
# print('Hello ' + family[-2])
# print('Hello ' + family[-3])

"""[summary]
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[0:4]
['cat', 'bat', 'rat', 'elephant']
>>> spam[1:3]
['bat', 'rat']
>>> spam[0:-1]
['cat', 'bat', 'rat']
"""

# example_10
# print(family[0:3])
# print(family[1:2])

"""
>>> spam = ['cat', 'dog', 'moose']
>>> len(spam)
3
"""
