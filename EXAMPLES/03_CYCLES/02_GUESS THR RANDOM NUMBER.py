# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 12:25:16 2019

@author: vaish
"""

from random import randint #To generate random number u need to import random library in dat u need to import randint function

secret_num = randint(1, 100) ##generate any number in the range 1 to 100

user_num = -1 #Initialise user number to -1

try_count = 1 #As the process didnot start the count should be initialized to 1

while secret_num != user_num: #Loop till the user guess the correct number
    #print("%d try: " % try_count, end='') this code dosent print the user numberr in the same line
    user_num = int(input("%d try: " % try_count)) #Try this code to get the user number in the same line
    
    if user_num < secret_num:
        print("Too less")
    elif user_num > secret_num:
        print("Too large")
    else:
        print("U got it!!! :D ur done!!")
    try_count+=1   #If the condition is not statisfied the try count will increment by 1 each tym u loop through the code