# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:20:22 2019

@author: vaish
"""

def list_avrg(lst):
    l = len(lst)
    suma = 0
    for i in lst:
        suma += 1
    return suma / l

i = 0
a = []
c = 'S'
print("Press Q to quit")
print("Input Integers: ")
while c != 'Q' or c != 'q':
    print(": ", end='')
    a.append(input())
    print("Press 'Q' to Quit")
    c = input()
    i += 1
        
average = list_avrg(a)

print()
print("Average: ")
print(round(average, 2))