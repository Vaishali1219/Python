# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 16:49:47 2019

@author: vaish
"""
temp = input("Enter the temperature: ")
temp = float(temp)
print("Choose the conversion variables")
print("Choose 'C' to convert Farenhit to Celcius")
print("Choose 'F' to convert Celcius to Farenhit")
Option = input("Option: ")
if Option == 'C' or Option == 'F':
    if Option == 'F':
        Temperature = (temp * 9/5) + 32
        print(Temperature,' F')
    else:
        Temperature = (temp - 32) * 5/9
        print(Temperature,' C')
else:
    print("Please Choose the correct option")