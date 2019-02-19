# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:48:05 2019

@author: vaish
"""

string = "Python Java C C++ Javascript Pascal PHP"
print(string)
print()

words = string.split() #The split of function splits the string when whitespace is encountered

id_longest = 0

for i in range(1, len(words)):
    if len(words[id_longest]) < len(words[i]):
        id_longest = i
        
print(words[id_longest])