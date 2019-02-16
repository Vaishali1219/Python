# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:54:14 2019

@author: vaish
"""

string = input("Enter a string: ")

length = len(string)

lower = upper = 0

for i in string:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
        
per_lower = lower / length * 100
per_upper = upper / length * 100
print("Lower: %.2f%%" % per_lower)
print("Upper: %.2f%%" % per_upper)
