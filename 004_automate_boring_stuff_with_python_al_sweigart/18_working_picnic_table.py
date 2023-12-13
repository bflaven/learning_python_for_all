#! python3



"""

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_000_python_for_family/002_learn_code_for_kids/automate_boring_stuff_with_python_al_sweigart

python3 18_working_picnic_table.py





https://automatetheboringstuff.com/#toc



"""


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items(): 
            print(k.ljust(leftWidth, '.') + str(v).rjus(rightWidth))
            picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
            
            
            printPicnic(picnicItems, 12, 5)
            
            # printPicnic(picnicItems, 20, 6)


        
        
        







