# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:55:16 2019

@author: vaish
"""
""" ASSIGNEMNT # 6: ADVANCED LOOPS :- A SCALABLE GRID WITH SHAPES
In this assignment I have tried printing grids with shapes(Triangles). More importatntly this pattern is scalable between
sizes 8 to 100.
The pattern will look like:
               |           |          
      @   |           |   @
     @@   |           |   @@
    @@@   |           |   @@@
     @@   |           |   @@          #3 x 3 matrix figure only
      @   |           |   @
          |           |               #Each major row is divided into blocks and subrows
--------- + --------- + ---------
          |           |          
          |           |          
          |           |          
          |           |          
          |           |          
          |           |          
          |           |          
--------- + --------- + ---------
          |           |          
      @   |           |   @
     @@   |           |   @@
    @@@   |           |   @@@
     @@   |           |   @@
      @   |           |   @
          |           |          
          
This figure is completely scaleable depending on the size you input.

As pattern includes shapes within the grids so I have used only row logic and no column logic is used.
"""
n = int(input("Enter the size Minimum size should be 8 and maximum 100: "))
if n % 2 == 0:
    N = n
else:
    N = n + 1
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







    
    
    
    
    
    
    
    
    
    