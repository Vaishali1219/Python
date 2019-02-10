# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:01:43 2019

@author: vaish
"""

a = abs(int(input('Enter a number: '))) #get the absolute value of the number which would turn negative num to positive

suma = 0 #Initialize suma to 0 and Mult to 1
mult = 1

while a > 0: #This will loop till a becomes less than or equal to zero
    digit = a % 10
    suma += digit
    mult *= digit
    a = a // 10 #This will turnaced a decimal no to integer
    
print("Sum: ", suma)
print("Product: ", mult)


