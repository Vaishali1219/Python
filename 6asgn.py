# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 21:11:27 2019

@author: vaish
"""
N = int(input("Enter the size Minimum size should be 9: "))
value = N // 2
base = 0
if N in range(8 , 101):
    for j in range(8, 101, 2):
        base += 1
        if j == N:
            break
 
count = value + base
p = 1
for block in range(1, 4):
    if block == 1:
        for row in range (1, (N + 1)):
            if row == 1 or row == (N - 1): #N - 2
                print(" " * (N + 1),"|"," " * (N + 1),"|"," " * (N + 1)) 
            elif row == (N):
                print("-" * (N + 1),"+","-" * (N + 1),"+","-" * (N + 1))
            else:
              
                if row in range(2, (value + 1)):
                    print(" " * count,"@" * p," ","|"," " * (N + 1),"|"," ","@" * p)
                    count -= 1
                    p += 1
                    if p == value:
                        p -= 2
                        count += 2
                elif row in range((value + 1), (N - 1)):
                    print(" " * count,"@" * p," ","|"," " * (N + 1),"|"," ","@" * p)
                    count += 1
                    p -=1
                    if p < 1:
                        count = value + base
                        p = 1
                    
    if block == 2:
        for row in range(1, (N + 1)):
            if row != N:
                print(" " * (N + 1),"|"," " * (N + 1),"|"," " * (N + 1))
            else:
                
                print("-" * (N + 1),"+","-" * (N + 1),"+","-" * (N + 1))
    if block == 3:
        for row in range (1, (N + 1)):
            if row == 1 or row == (N - 1): #N - 2
                print(" " * (N + 1),"|"," " * (N + 1),"|"," " * (N + 1)) 
            else:
              
                if row in range(2, (value + 1)):
                    print(" " * count,"@" * p," " * 1,"|"," " * (N + 1),"|"," " * 1,"@" * p)
                    count -= 1
                    p += 1
                    if p == value:
                        p -= 2
                        count += 2
                elif row in range((value + 1), (N - 1)):
                    print(" " * count,"@" * p," " * 1,"|"," " * (N + 1),"|"," " * 1,"@" * p)
                    count += 1
                    p -=1
        
                    
                    
            
    
                
           