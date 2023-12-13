#! python3


"""

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_000_python_for_family/002_learn_code_for_kids/automate_boring_stuff_with_python_al_sweigart

python3 12_working_with_loops.py

https://automatetheboringstuff.com/#toc



"""

# example_1
# for i in range(15):
#     print(i)


# example_2
# for i in [0, 1, 2, 3, 4, 5, 6, 7]:
#   print(i)

"""
# 'stylos', 'agrafes', 'lance-flammes', 'classeurs'
>>> supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
>>> for i in range(len(supplies)):
print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

african_capitals = ['Niamey', 'Tunis', 'Maputo', 'Nouakchott', 'Asmara', 'Bamako', 'Abuja', 'Juba', 'Kampala']

# Niamey, Niger
# Tunis, Tunisia
# Maputo, Mozambique
# Nouakchott, Mauritania
# Asmara, Eritrea
# Bamako, Mali
# Abuja, Nigeria
# Juba, South Sudan
# Kampala, Uganda



"""

african_countries = ['Niger', 'Tunisia', 'Mozambique',
                     'Mauritania', 'Eritrea', 'Mali', 'Nigeria', 'South Sudan', 'Uganda']

african_capitals = ['Niamey', 'Tunis', 'Maputo', 'Nouakchott',
                    'Asmara', 'Bamako', 'Abuja', 'Juba', 'Kampala']

for i in range(len(african_capitals)):
    print('Index ' + str(i) +
          ' :: The African countrie is ' + african_countries[i] + ' :: The Capital is ' + african_capitals[i])




