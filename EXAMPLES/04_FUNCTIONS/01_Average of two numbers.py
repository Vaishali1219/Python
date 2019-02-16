# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:11:34 2019

@author: vaish
"""

def avg(a, b):
    av = (a + b) / 2
    return av

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

avrg = avg(x , y)
print()
print("The average is %2.5f" % avrg)