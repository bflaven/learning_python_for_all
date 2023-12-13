#!/usr/bin/python
# -*- coding: utf-8 -*-
#


"""
https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md#the-world


python --version
# Python 2.7.10

python3 --version
# Python 3.7.7



cd /Users/brunoflaven/Documents/02_copy/_000_IA_bruno_light/_learn_code_for_kids/python_by_example/

python 15_scripts_for_kids_tkinter_gui_124_132.py
python3 15_scripts_for_kids_tkinter_gui_124_132.py

"""


from tkinter import *

def Call():
    msg = Label (window, text = "Fuck, you pressed this button")
    msg.place(x=30, y=50)
    button["bg"] = "red"
    button["fg"] = "white"
    
window = Tk()
window.geometry("500x400")
button = Button (text="Yolo, press me", command = Call)
button.place(x=30, y=20, width=220, height=50)
window.mainloop()


    
