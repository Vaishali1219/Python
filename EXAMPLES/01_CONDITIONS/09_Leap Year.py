# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 05:39:26 2019

@author: vaish
"""

year = int(input("Enter the year: "))
if year % 4 != 0:
    print("Normal Year")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Leap year")
    else:
        print("Normal year")

else:
    print("Leap Year")