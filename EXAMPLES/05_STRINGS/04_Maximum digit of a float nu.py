# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:48:58 2019

@author: vaish
"""

from random import *

num = round(random() * 100, 3)
print(num)

strNum = str(num)

maxDigit = -1

for i in range(len(strNum)):
    if strNum[i] == '.':
        continue
    elif maxDigit < int(strNum[i]):
        maxDigit = int(strNum[i])

print(maxDigit)
