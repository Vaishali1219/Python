# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:46:34 2019

@author: vaish
"""

def reverse_words(s):
    s = s.split()
    seq = reversed(s)
    fin = (" ".join(seq))
    return fin
    
print("Enter your String: ")
print(reverse_words(input()))