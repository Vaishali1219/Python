# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:56:36 2019

@author: vaish
"""
def list_avrg(lis):
    l = len(lis)
    suma = 0
    for j in range(l):
        suma += lis[j]
    ag = suma / l
    return ag


print("Input integers:")
a = input()
a = a.split() #while inputing values please add space
for i in range(len(a)):
    a[i] = int(a[i])
    
#print(len(a))

##for i in range(len(a)):
#    print(a[i])
    
avg = list_avrg(a)

print()
print("Average: ")
print(round(avg, 2))