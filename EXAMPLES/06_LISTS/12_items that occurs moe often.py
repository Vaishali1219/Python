# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:36:42 2019

@author: vaish
"""

from random import *

a = [int(random() * 5) for i in range(15)]
print(a)
print()

a_set = set(a) #This function will return a new set

most_common = None
qty_most_common = 0

for item in a_set:
    qty = a.count(item) #This function will return the number of times an item occur in a list
    if qty > qty_most_common:
        qty_most_common = qty
        most_common = item
        
print(most_common," occurs ",qty_most_common," times ")