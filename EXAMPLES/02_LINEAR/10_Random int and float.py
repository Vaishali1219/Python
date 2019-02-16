# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:03:34 2019

@author: vaish
"""

#From random module, we import
#the random() function, which generates
#a random float number, and
#the randint() function,
#which generates a random integer



from random import *

#We request the lower and upper limits of the range
#within these limits a random integer will be generated

print("Range of integers: ")
imin = int(input("Minimum =  "))
imax = int(input("Maximum =  "))

n = randint(imin, imax)

print()
print("%d" % n)


#We request the lower and upper limits of the range, within these limits a random float will be generated
print()
print("Range of floats: ")
fmin = float(input("Minimum =  "))
fmax = float(input("Maximum =  "))

m = random() * (fmax - fmin) + fmin


"""The random() function generates a float number from 0 to 1. The 1 is not in the range
Multiply the number by length of the range. If fmax = 5.6, fmin = 3.2, then we get a random number from 0 to 2.4
Shift the lower limit by the value fmin. Thus the random number will be in the range 3.2 to 5.6"""


print()
print("%.3f" % m)