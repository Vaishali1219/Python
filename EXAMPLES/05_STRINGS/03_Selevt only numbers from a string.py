# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 06:35:43 2019

@author: vaish
"""
#Ex: ABC25 - l = 5
s = input("Enter a string with alphabets and letters: ")
l = len(s) #Get the length of the string

i = 0 
while i < l: 
    num = ''
    symbol = s[i]
    while symbol.isdigit(): #This will return true if the symbol is a digit else false
        num += symbol
        i += 1
        if i < l:
            symbol = s[i]
        else:
            break
    if num != '':
        print(num)
    i += 1
    