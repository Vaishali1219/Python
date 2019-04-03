# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:03:51 2019

@author: vaish
"""

class person:
    def __init__(self, person_name, person_surname):
        self.name = person_name
        self.surname = person_surname #Class Constructor
        
    def about(self):
        return self.name + ' ' + self.surname
    
men = []
for i in range(5):
    one = input("Enter the person name: ")
    one = one.split() #Splits the string in words
    men.append(person(one[0], one[1]))
    
for i in men:
    print(i.about())
    