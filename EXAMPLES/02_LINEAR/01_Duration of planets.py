# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 05:56:55 2019

@author: vaish
"""

import math

r = float(input("Radius of the orbit (million km): "))
v = float(input("Orbital speed in (km/s): "))

r = r * 1000000

year = 2 * pi * r / v

year = year / (60 * 60 * 24)

print(round(year))