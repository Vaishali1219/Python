# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:52:56 2019

@author: vaish
"""

import math
n = int(input("Enter the number: "))
if n < 2:
    print("A number should be greater than 2")
    quit()
elif n == 2:
    print("It's a Prime Number")
    quit()
    
i = 2

limit = int(math.sqrt(n))

while i <= limit:
    if n % i == 0:
        print("its a Composite number")
        quit()
    i += 1
    
print("its a prime number")