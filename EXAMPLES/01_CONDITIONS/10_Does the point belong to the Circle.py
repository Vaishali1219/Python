# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 05:39:25 2019

@author: vaish
"""

import math

print("Point: ")
x = float(input("x = "))
y = float(input("y = "))
print("Radius of the Circle: ")
r = float(input("r = "))

hyp = math.sqrt(pow(x , 2) + pow(y , 2))

#hyp = math.sqrt(x**2 + y**2)
#hyp = math.sqrt(math.pow(x , 2) + math.pow(y , 2))

if hyp <= r:
    print("The point belongs to the Circle")
else:
    print("The point doesn't belong to the Circle")
    
    