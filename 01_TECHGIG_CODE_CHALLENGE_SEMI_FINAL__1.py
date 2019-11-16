# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:16:46 2019

@author: vaish
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#a = [3, 5, 7, 2]   #17
#a = [121, 23, 3, 333, 4] #458
#a = [1, 2, 12, 13, 25] ##38
#a = [32, 42, 52, 62, 72, 82, 92] #92

def main():
    test = True

    while test == True:
        T = input()
        T = int(T)
        if T > 0 and T < 6:
            test = False
        
    v = 0
    result = []
    sums = []

    while v < T:
    
        while test == False:
            N = int(input())
            if N > 0 and N <= 101:
                test = True
            
        a = [int(x) for x in input().split() [:N] if int(x) > 0 and int(x) <= 100000]   #
        a.sort(reverse = True)
        b = a.copy()
        w = [""] 
        i = 0
        while w != []:
            w = []
            while i < len(a):
                r = False
                if a[i] in b:
                    temp = str(a[i]) 
                    for j in temp:
                        for k in range(len(a)): 
                            if k == i: 
                                continue
                            else:
                                if a[k] in b: 
                                    x = a[k] 
                                    while (x > 0):
                                        if (x % 10 == int(j)):
                                            r = True
                                            break
                                        x = x // 10
                                    if r: 
                                        if a[k] not in w:
                                            w.append(a[k]) 
                                        if a[k] in  b:
                                            b.remove(a[k])
                                r = False
                        r = False
                i += 1
            sums.append(sum(b))
            b = w.copy()
            a = w.copy()
            i = 0
            
        
        result.append(max(sums))  
        v += 1
        test =  False
        sums = []

            
    for i in range(len(result)):
        print(result[i])  



main()
