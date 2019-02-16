# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 06:45:14 2019

@author: vaish
"""

print("Enter the co-ordinates of the point below")
x = float(input("x = "))
y = float(input("y = "))

if x > 0 and y > 0:
    print("Ist Quadrant")
elif x < 0 and y > 0:
    print("IInd Quadrant")
elif x < 0 and y < 0:
    print("IIIrd Quadrant")
elif x > 0 and y < 0:
    print("IVth Quadrant")
elif x == 0 and y == 0:
    print("The point is at the Origin")
elif x == 0:
    print("The point is on Y-axis")
else:
    print("The point is on X-axis")