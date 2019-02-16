# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:58:36 2019

@author: vaish
"""

s = input("Enter a string: ")

l = len(s)

for i in range(l // 2):
    if s[i] != s[-1 - i]:
        print("Its not a plaindrome")
        quit()
        
print("Its a plaindrome")