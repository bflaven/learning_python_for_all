#! python3


"""

cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_000_python_for_family/002_learn_code_for_kids/automate_boring_stuff_with_python_al_sweigart

python3 09_magic8Ball.py

https://automatetheboringstuff.com/#toc



"""


import random

def getAnswer(answerNumber):
        if answerNumber == 1:
            return 'It is certain'
        elif answerNumber == 2:
            return 'It is decidedly so'
        elif answerNumber == 3:
            return 'Yes'
        elif answerNumber == 4:
            return 'Reply hazy try again'
        elif answerNumber == 5:
            return 'Ask again later'
        elif answerNumber == 6:
            return 'Concentrate and ask again'
        elif answerNumber == 7:
            return 'My reply is no'
        elif answerNumber == 8:
            return 'Outlook not so good'
        elif answerNumber == 9:
            return 'Very doubtful'

# output_1 3 lines
# r = random.randint(1, 9)
# fortune = 
# print(fortune)

# output_2 3 lines
print(getAnswer(random.randint(1, 9)))
