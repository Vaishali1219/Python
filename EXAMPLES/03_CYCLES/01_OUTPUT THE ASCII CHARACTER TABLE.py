# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 12:18:00 2019

@author: vaish
"""

for i in range(32, 128): #This line of code will loop from ASCII value 32 till 127
    print(chr(i),'\t', end='') #This line will print only 10 characters in a line
    if (i-1) % 10 == 0: #This if statement is for checking out whether 10 characters are printed or not
        print()
        

