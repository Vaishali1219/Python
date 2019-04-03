# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:20:33 2019

@author: vaish
"""

import sqlite3

MySchool = sqlite3.connect('schooltest.db')
#curschool.execute("""CREATE TABLE students (
#    studentID   INTEGER PRIMARY KEY AUTOINCREMENT,
#    Name      TEXT (20) NOT NULL,
#    House    TEXT,
#    Marks REAL);""")
nm = input("Enter Name: ")
"""mysid = int(input("Enter Id: "))
myname = input("Enter name: ")
myhouse = int(input("Enter the house number: "))
mymarks = float(input("Enter marks: "))

try:
    curschool = MySchool.cursor() #A python object that enables to connect to db, returns a cursor object
    curschool.execute("INSERT INTO students (studentID, Name, House, Marks) VALUES (?,?,?,?);", (mysid,myname,myhouse,mymarks))
    MySchool.commit()
    print("record added successfully")

except:
    print("Error in Operation")
    MySchool.rollback()
    
MySchool.close()"""

sql = "SELECT * from students WHERE Name = '"+nm+"';"
curschool = MySchool.cursor() #A python object that enables to connect to db, returns a cursor object
curschool.execute(sql)
record = curschool.fetchone()
print(record)

res = input("Do you want to delete this record? (Y/N)")
sql = "DELETE from students WHERE Name = '"+nm+"';"
if res == 'Y':
    try:
        curschool.execute(sql)
        MySchool.commit()
        print("Record Deleted Successfully")
    except:
        print("Error in update operation")
        MySchool.rollback()
MySchool.close()

"""while True:
    record = curschool.fetchone()
    if record == None:
        break
    print(record)"""
    
"""result = curschool.fetchall()
for record in result:
    print(record)"""
    

    


