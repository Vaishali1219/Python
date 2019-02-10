# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:23:48 2019

@author: vaish
"""

num = abs(int(input("Enter the number: ")))
Even = 0
Odd = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        Even += 1
    else:
        Odd += 1
    num //= 10
print("The number of Even Digits is: ", Even)   
print("The number of Odd Digits is: ", Odd)     
