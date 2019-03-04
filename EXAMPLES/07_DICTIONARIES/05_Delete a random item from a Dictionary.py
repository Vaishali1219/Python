# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:56:31 2019

@author: vaish
"""

import random

d = {"A": 4, "O": 6, "P": 10, "M": 7, "B": 3}

print(d)

keys = list(d.keys())
what_del = random.choice(keys)
del d[what_del]
print(d)