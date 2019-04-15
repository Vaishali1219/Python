# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:21:52 2019

@author: vaish
"""

import sqlite3

def decor(UI, UQ, P, T):
    header = "Vaish Book Center"
    Menu = "Tile          Price          Quantity          Total"
    length = len(Menu)
    print("=" * length)
    print(" " * int(length/3),header," " * int(length/2))
    print("=" * length)
    print(Menu)
    print("-" * length)
    print("{}           {}              {}                {}".format(UI, P, UQ, T))
    print("-" * length)
    print()
    return
    
UserIn = input("Enter the users choice: ")
UserQu = int(input("Enter the number of copies required: "))
MyBook = sqlite3.connect('books.db')
sql = "SELECT Price from Books where Title == '{}';".format(UserIn)
curbuk = MyBook.cursor()
curbuk.execute(sql)
while True:
    record=curbuk.fetchone()
    if record==None:
        break
    price = int(record[0])
    print()
    print("Book Cost = {}".format(price))
Total = UserQu * price
print()
decor(UserIn, UserQu, price, Total)
MyBook.close()


