# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:54:24 2019

@author: vaish
"""

string = input("Write down a text:\n")

signs = ['.', ',', ':', ';', '!', '?', '(', ')']

words = string.split()

i = 0
for word in words:
    if word[-1] in signs:
        word[i] = word[: -1]
        word = words[: i]
    if word[0] in signs:
        words[i] = word[1:]
    i += 1
    
for i in words:
    print(i, end='')
print()