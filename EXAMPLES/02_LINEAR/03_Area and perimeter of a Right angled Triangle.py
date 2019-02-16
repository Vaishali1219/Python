# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 06:05:00 2019

@author: vaish
"""

import math

AB = float(input("Length of the first side: "))
AC = float(input("Length of the second side: "))

BC = math.sqrt(AB**2 + AC**2)

S = (AB * AC) / 2
P = AB + AC + BC

print("The area of the triangle: %.2f" % S)
print("The perimeter of the triangle: %.2f" % P)