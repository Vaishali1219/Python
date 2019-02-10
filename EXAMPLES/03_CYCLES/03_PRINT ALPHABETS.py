# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 12:39:57 2019

@author: vaish
"""

first_letter = input("The first letter: ") #get the range of letters to be printed
last_letter = input("The last letter: ")

while ord(first_letter) <= ord(last_letter): #Loop til the ASCII value of first letter becomes equal to last
    print(first_letter,'\t', end='') #Print a letter followed by tab space and one beside the other
    first_letter = chr(ord(first_letter) + 1) #Increment to next letter by first fetching the ASCII value of next letter and truning it back to the character value
print()