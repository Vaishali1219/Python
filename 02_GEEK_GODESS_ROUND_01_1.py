# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:11:09 2019

@author: vaish
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    count = 0
    jud = {}
    test = True
    p=[]
    while test == True:
        T = int(input())
        if T > 0 and T < 11:
            test = False

    V = 0
    while V < T:
        while test == False:
            N = input()
            S = list(N)
#            print(S)
            if len(S) > 0 and len(S) <= 100000:
                test = True
            B = set(S)
#            print(B)
            for x in B:
                if S.count(x) >= count:
                    count = S.count(x)
                    temp = ord(x)
                    jud[temp] = count
            count = 0
            s = sorted(jud.items(), key=lambda x:x[1], reverse=True)
            m = int(s[0][1])
            e = [k for k,o in jud.items() if o == m]
            e.sort()
#            print(jud)
#            print(s)
#            print(e)
            p+=chr(e[0])
#            print(p)
            V += 1
            s = []
            jud={}
            count = 0
        test = False

    for x in p:
        print(x)

main()