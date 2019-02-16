# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 06:52:11 2019

@author: vaish
"""

print("Enter the length of the sides below:")
a = float(input("a =  "))
b = float(input("b =  "))
c = float(input("c =  "))

if a + b > c and a + c > b and b + c > a:
    print("The triangle Exists")
else:
    print("The triangle doesn't Exists")