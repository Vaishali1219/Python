# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:45:37 2019

@author: vaish
"""

from math import *

r = float(input("Enter the radius of the Circle: "))

a = pi * r**2
c = 2 * pi * r

print()
print("The area of the circle with radius %2.2f is %2.2f" % (r, a))
print()
print("The circumference of the circle with radius %2.2f is %2.2f" % (r, c))
