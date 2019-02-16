# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:56:31 2019

@author: vaish
"""

n1 = '3'
n2 = '8'

a = ord(n1)
b = ord(n2)

diff = a - b
total = a - ord('0') + b - ord('0')

print("%s - %s = %d" % (n1, n2, diff))
print("%s + %s = %d" % (n1, n2, total))