# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 06:10:14 2019

@author: vaish
"""

from random import *

n = randint(100, 999)
n = int(n)
print(n)
print()

s = str(n)

a = int(s[0])
b = int(s[1])
c = int(s[2])

print("Sum is %d" % (a + b + c))