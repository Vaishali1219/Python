# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 13:54:01 2019

@author: vaish
"""

i=1
count=1
num=10
n = input('Enter the range: ')
n = int(n)
mod = n % 10
length= n/10 + 1
if (mod == 0):
    print("\n")
    while(count<length):
        for j in range(i, num+1):
            print(range(j, j+10))
            
        count+=1
        num+=10
        print('\n')
else:
    print('\n')
    length = length - 1
    while(count<length):
        for k in range(i, num+1):
            print(k, '\t')
        count+=1
        num+=10
        print("\n")
    count = 1
    while(count<mod):
        for l in range (i, n+1):
            print(i, "\t")
        count+=1
        print("\n")
            
        
	      
	             
	       
	       
	      