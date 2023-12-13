#!/usr/bin/python
# -*- coding: utf-8 -*-
#


"""
https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md#the-world


python --version
# Python 2.7.10

python3 --version
# Python 3.7.7


cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_learn_code_for_kids/python_for_teenagers/

python3 FunWithFiles.py
"""


# This code is used to open a file
# However, since the file does not already exist
# Python instead creates it for us
# Remember, if the file name already exists, it will overwrite the existing one, erasing its contents in the process.
newFile = open("CreatedFile.txt", 'w')

# This code is similar to a print() statement
# However, instead of writing text or output to a user's computer screen
# It writes it to a file instead

newFile.write("Look, we created a brand new file using Python code!")
newFile.write("\nHere is a second line of text!")
newFile.write("\n Nous c'est Louise et Arthur")

# The close() function closes the file we are working on and saves it
# It is important to always close a file when we are finished with it
# To ensure we do not make any additions or mess up the file in anyway

newFile.close()
print ("File created and written!")




