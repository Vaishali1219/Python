# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:19:16 2019

@author: vaish
"""

goods = {"Apple": [4.5, 10], "Orange": [6.2, 5], "Pineapple": [10.0, 1], "Mango": [7.5, 2], "Banana": [3.8, 10]}

for key, value in goods.items():
    print(key," - ", value[0], '-', value[1])
    
print()
print()
    
cost = 0

while True: 
    good = input("What? (n - nothing): ")
    if good == 'n':
        break
    qty = int(input("How many? "))
    if qty > goods[good][1]:
        print("We don't have so much.")
        continue
    cost += goods[good][0] * qty
    goods[good][1] -= qty
    
print()
print("Price: ", cost)

for key, value in goods.items():
    print(key,'-', value[0],'-', value[1])