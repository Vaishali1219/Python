# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:14:45 2019

@author: vaish
"""

n = int(input("Number of items: ")) #First get the number of numbers you want to display

item = 1 #Set the first number of the series as 1

while n > 0: #Till the number of items becomes equal to or less than 0 this loop will continue
    print(item,'\t', end='') #This code is for printing the items in the same line
    item /= -2
    n -= 1
    
print()

"""This is a series where each number will be multiplied by -0.5"""