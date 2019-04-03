# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:51:58 2019

@author: vaish
"""

class A:
    class_field = 10 #class atributes which can be called by class only
    
    def method(self, value):
        self.obj_field = A.class_field + value
        
a1 = A()
a2 = A()

a1.method(3)
a2.method(100)

print(a1.obj_field) #obj_filed is an instance attribute so can be called by objects.
print(a2.obj_field)

print(A.class_field) #since class_field is a class atributeit can called through class only