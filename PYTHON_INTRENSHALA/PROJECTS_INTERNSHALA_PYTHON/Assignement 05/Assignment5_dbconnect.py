# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 16:30:24 2019

@author: vaish
"""

import sqlite3
"""MyBook = sqlite3.connect('books.db')
curbuk = MyBook.cursor()
curbuk.execute('''CREATE TABLE Books (
Book_ID INTEGER PRIMARY KEY AUTOINCREMENT,
Title TEXT (20) NOT NULL,
Author TEXT(20),
Price REAL);''')
MyBook.close()""" 

MyBook = sqlite3.connect('books.db')
curbuk = MyBook.cursor()
n = int(input("How many rows of data u need to enter: "))
for i in range(n):
    Title = input("Title : ")
    Author = input("Author: ")
    Price = int(input("Price: "))
    curbuk.execute("INSERT INTO Books (Title, Author, Price) VALUES ('{}', '{}', {});".format(Title, Author, Price))

MyBook.commit()

MyBook = sqlite3.connect('books.db')
sql = "SELECT * from Books;"
curbuk = MyBook.cursor()
curbuk.execute(sql)
result=curbuk.fetchall()
for record in result:
    print("-----------------------------------------------")
    print ("Title => {}".format(record[1:2]))
    print ("Author => {}".format(record[2:3]))
    print ("Price => {}".format(record[3:]))
    print("-----------------------------------------------")
    print()   
MyBook.close()