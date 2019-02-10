# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 13:11:19 2019

@author: vaish
"""

print("Zero as an operatio sign will terminate the program")
DO = True
while DO == True:
     s = input("Sign(+, -, *, /): ")
     if s == '0': break
     if s in ('+', '-', '*', '/'):
         x = float(input("x = "))
         y = float(input("y = "))
         if s == '+':
             print(x,' + ',y,' = ',(x + y))
         elif s == '-':
             print(x,' - ',y,' = ',(x - y))
         elif s == '*':
            print(x,' * ',y,' = ',(x * y))
         elif s == '/':
             if y != 0:
                print(x,' / ',y,' = ',(x / y))
             else:
                 print("Division by zero!")
     else:
         print("invalid Operation Sign!")
             