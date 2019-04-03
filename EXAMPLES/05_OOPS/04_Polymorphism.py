# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:21:13 2019

@author: vaish
"""

class T1:
    n = 10
    
    def total(self, N):
        print(int(self.n) + int(N))
        
class T2:
    def total(self, s):
        print(len(str(s)))
        
t1 = T1()
t2 = T2()

t1.total(45)
t2.total(45)