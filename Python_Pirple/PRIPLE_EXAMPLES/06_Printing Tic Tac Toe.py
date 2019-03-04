# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 06:18:34 2019

@author: vaish
"""

"""Creating a Tic Tac Toe"""
#01234
# | |  0
#----- 1
# | |  2
#----- 3
# | |  4

for row in range(5):
    if row % 2 == 0:
        for column in range(0, 5):#01234
            if column % 2 == 0:
                if column != 4:
                    print(" ",end='')#024
                else:
                    print(" ")
            else:
                print("|", end='')#13
    else:
        print("------")
        

        
        