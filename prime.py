# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 13:08:19 2019

@author: vaish
"""

def checkPrime(n):
    Flag = 0
    for x in range(2, n):
        if (n % x) == 0:
            Flag = 1
            break
    return (Flag)
        
    

m = input('Enter the number: ')
m = int(m)
F = checkPrime(m)
if F == 1:
    print('Composite')
else:
    print('Prime')