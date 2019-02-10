# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 12:48:50 2019

@author: vaish
"""

i = 1 #Initialize to 1 as we are starting from 1
while i < 10: #Loop only 9 times to print tables from 1 to 9
    j = 1 #This is to print only 10 values a row e.g till 1 * 10 = 10
    while j <= 10: #This will loop 10 times
        print("%4d" % (i * j), end='')
        j += 1 
    print()
    i += 1

"""This is a Multiplication Table using While loop"""