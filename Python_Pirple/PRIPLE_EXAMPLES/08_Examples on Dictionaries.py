# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 06:09:44 2019

@author: vaish
"""

BlackShoes = {42:2, 41:3, 40:4, 39:1, 38:0}
while(True): #True == True
    purchaseSize = int(input("Which shoe size would you like to buy?\n"))
    if purchaseSize < 0:
        break
    if BlackShoes[purchaseSize] > 0:
        BlackShoes[purchaseSize] -= 1
    else:
        print("Size Out Of Stock")
        print()
    print(BlackShoes)


    
    
    