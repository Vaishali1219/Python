# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:42:38 2019

@author: vaish
"""

n1 = int(input("An Integer: "))
n2 = 0

while n1 > 0:
    digit = n1 % 10
    n1 //= 10
    n2 = n2 * 10
    n2 = n2 + digit

print("Inverse number: ", n2)