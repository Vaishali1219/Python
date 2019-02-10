# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 12:57:02 2019

@author: vaish
"""

num = int(input("Enter the number: ")) #Get the number and its base value
base = int(input("Enter the base (2 - 9): "))
if not(2 <= base <= 9): #Check if the base is in the specified range
    print("Invalid base") #If not the program will exit
    quit()

newNum = '' #Initilse the newNum as a blank string
while num > 0: #till the number is gretaer than zero this will loop
    newNum = str(num % base) + newNum 
    num //= base
    
print("",newNum)
