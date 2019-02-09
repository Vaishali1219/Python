# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:45:27 2019

@author: vaish
"""
##printing a simple triangle
Length = 100
ToPrint = '$'
for pos in range(1, Length+1):
    print(ToPrint*pos)
for pos in range(Length, 0, -1):
    print(ToPrint*pos)