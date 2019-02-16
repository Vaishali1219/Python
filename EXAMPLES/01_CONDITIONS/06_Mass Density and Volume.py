# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 06:38:29 2019

@author: vaish
"""

result  = None

flag = input("What to Calculate? (m , d, v): ")
if flag == 'm':
    d = float(input("Density: "))
    v = float(input("Volume: "))
    result = d * v
elif flag == 'd':
    m = float(input("Mass: "))
    v = float(input("Volume: "))
    result = m / v
elif flag == 'v':
    m = float(input("Mass: "))
    d = float(input("Density: "))
    result = m / d
else:
    print("Wrong Option")
    quit()

print("%.2f" % result)
    