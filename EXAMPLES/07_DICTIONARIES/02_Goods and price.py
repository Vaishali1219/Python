# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:56:13 2019

@author: vaish
"""

goods = {"Apple": 4.5, "Orange": 6.2, "Pineapple": 10.0, "Mango": 7.5, "Bananna": 3.8}

for good, price in goods.items():
    print(good," - ",price)
    
cost = 0

while True:
    good = input("What? (n - nothing): ")
    if good == 'n':
        break
    qty = int(input("How many? "))
    cost += goods[good] * qty
    
print("Price: ", cost)