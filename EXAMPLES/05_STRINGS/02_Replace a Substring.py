# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 06:17:18 2019

@author: vaish
"""

things = "tree, box, chair, lamp, desk, cat, dog, grass, pig, box, lamp, shelf" #First declare a string
         
print(things) #Print the string for refernce
print()

old_item = input("Old_item: ") #Get the item of the string to be replaced
new_item = input("New_item: ") #Get the new String
len_old_item = len(old_item) #Get the length of the string to be replaced

i = things.find(old_item) #If the item to be replaced is found in the string the find() function will return its index Ex: chair if found the function will return 11
while i > 0: #Now chair is in 11 so i = 11 and now i(11) > 0 so the while loop will execute
    before = things[:i] #Before is item of the string things till i(11) i.e til box,' '
    after = things[i + len_old_item:] #Aftre is items after the word chair so will leave a space = 11 + 4 = 15 spaces so after string will be from index 15
    things = before + new_item + after #Now things is a combination of before, new string and after string
    i = things.find(old_item) #To terminate the loop i should become less than 0. As the old item is now removed the find() will return -1 and the loop will terminate

print()
print(things)  #Print the updated string  