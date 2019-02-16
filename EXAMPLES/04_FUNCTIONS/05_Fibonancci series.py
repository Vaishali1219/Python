# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:12:56 2019

@author: vaish
"""

"""def fib_n(item):
    f1 = f2 = 1
    while item > 2:
        buff = f2
        f2 = f1 + f2
        f1 = buff
        item -= 1
    return f2

def fib_row(item):
    f1 = f2 = 1
    print(f1, f2," ", end='')
    while item > 2:
        buff = f2
        f2 = f1 + f2
        f1 = buff
        print(f2," ", end='')
        item -= 1
    print()
    
n = int(input(": "))
m = fib_n(n)

print()
print(m)

fib_row(n)"""




n = int(input("Enter the length of the series: "))
a = [1 , 1]
for i in range (2 , n):
    a.append('')
for i in range(2, n):
    a[i] = a[i - 1] + a[i - 2]
    
print()
print(a)
    
    