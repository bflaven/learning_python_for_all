#! python3


"""

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_000_python_for_family/002_learn_code_for_kids/automate_boring_stuff_with_python_al_sweigart

python3 12_working_with_list_good.py

https://automatetheboringstuff.com/#toc



"""

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames)+1) +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
        catNames = catNames + [name]  # list concatenation
        print('The cat names are:')
        for name in catNames:
                print(' ' + name)
