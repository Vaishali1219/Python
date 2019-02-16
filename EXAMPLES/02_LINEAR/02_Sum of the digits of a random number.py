# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 06:00:29 2019

@author: vaish
"""

#from random import random

from random import *

n = random() * 900 + 100
n = int(n)
print(n)

a = n // 100
b = (n // 10) % 10
c = n % 10

print("\n")
print(a + b + c)