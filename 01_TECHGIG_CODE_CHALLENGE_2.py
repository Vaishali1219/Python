# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:49:59 2019

@author: vaish
"""
def get_result(ls):
    total = " "
    for p in range((len(ls) - 1), -1, -1):
        if ls[p] > 0:
            total += str(ls[p])
    return total

test = True
while test == True:
    T = int(input())
    if T > 0 and T < 11:
        test = False
        
T_1 = []
T_2 = []
T_Lis = []
sum_Lis = []
res_Lis = []
sum = 0
for n in range(T):
    while test == False:
        N = int(input())
        if N > 0 and N <= 10000:
            test = True
            
    T_Lis = [int(x) for x in input().split() [:N]] 
    
    for i in T_Lis:
        if i < -1000 and i > 1000:
            T_Lis[i] = 0
    
    if len(T_Lis) != N:
        for k in range(N - len(T_Lis)):
            T_Lis.append(0)


    for j in range(0, N, 2):
        sum += T_Lis[j]
        if T_Lis[j] > 0:
            T_1.append(T_Lis[j])
    sum_Lis.append(sum)
    sum = 0
    
    for k in range(1, N, 2):
        sum += T_Lis[k]
        if T_Lis[k] > 0:
            T_2.append(T_Lis[k])
    sum_Lis.append(sum)
    sum = 0
    
    if sum_Lis[0] == sum_Lis[1]:
            if min(T_1) > min(T_2):
                res_Lis.append(get_result(T_1))
            else:
                res_Lis.append(get_result(T_2))
    else:
        if sum_Lis.index(max(sum_Lis)) == 0:
            res_Lis.append(get_result(T_1))
        else:
            res_Lis.append(get_result(T_2))
            
    T_1 = []
    T_2 = []
    T_Lis = []
    sum_Lis = []
    sum = 0
    test =  False

for i in range(len(res_Lis)):
    print(res_Lis[i].lstrip())
        
    

    
        
        
        
        
        