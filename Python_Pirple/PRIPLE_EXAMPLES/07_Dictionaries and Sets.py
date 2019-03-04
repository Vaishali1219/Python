# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 06:14:07 2019

@author: vaish
"""

Sets = {"Element1", "Element2","Element1","Element4"}

print(Sets)
print()

if "Element1" in Sets:
    print("Yes")
    
CountryList = []
for i in range(5):
    Country = input("Please Enter your Country: ")
    CountryList.append(Country)

#CountrySet = set(CountryList)

#print(CountryList)
#print(CountrySet)

#if "Brazil" in CountrySet:
#    print("Attended")
    
#Dictionary = {"Key":"Value", "Key2":"Value2","Key3":"Value3"} #No repetition allowed as in sets
 
CountryDictionary = {}
for Country in CountryList:
    if Country in CountryDictionary:
        CountryDictionary[Country] += 1
    else:
        CountryDictionary[Country] = 1
        
print(CountryDictionary)

