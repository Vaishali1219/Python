# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 07:06:21 2019

@author: vaish
"""

test = True

while test == True:
    T = input("Enter TestCases: ")
    T = int(T)
    if T > 0 and T < 11:
        test = False
    
v = 0
result = []
V = []
P = []
res = 0

while v < T:
   
    while test == False:
        N = int(input("Enter the number of Players and Villans: "))
        if N > 0 and N <= 1000:
            test = True
        
        s = [int(x) for x in input().split()]   
        e = [int(x) for x in input().split()]
        for n in range(len(s)):
            V.append(s[n])
            P.append(e[n])
            
    V.sort()
    P.sort()
    
    for i in range(N):
        a = P[i]
        b = V[i]
        if a > b:
            res += 1
        else:
            continue
    
    if res == N:
        result.append("WIN")
    else:
        result.append("LOSE")
        
    v += 1
    test =  False
    V = []
    P = []
    res = 0
        

print()

for i in range(len(result)):
    print(result[i])
    
