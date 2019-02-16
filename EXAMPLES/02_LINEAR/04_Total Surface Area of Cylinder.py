# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:01:44 2019

@author: vaish
"""

from math import *

h = float(input("h = "))
r = float(input("r = "))

circles = 2 * (pi * r**2)
side = 2 * pi * r * h
area = circles + side

print()
print("A = ", round(area, 2))

