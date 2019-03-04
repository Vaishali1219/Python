# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 06:27:13 2019

@author: vaish
"""

word = "Hello"
Letters = []
for d in word:
    print(d)
    if d=="e":
        print('what a funny letter')
    Letters.append(d)
print(Letters)

for x in Letters:
    print(x)
    
Num = [1, 2, 3, 4 , 5]
for y in Num:
    if y%2 == 1:
        print(y)
Nat = []
Even = []  
Odd = []     
for p in range(10):
    Nat.append(p)
    if p%2==0:
       Even.append(p) 
    else:
        Odd.append(p)
print(Even)
print(Nat)
print(Odd)
Five = []
for z in range(1, 20, 5):
    Five.append(z)
print(Five)
Neg = []
for v in range(-1, -12, -3):
    Neg.append(v)
print(Neg)
    
     