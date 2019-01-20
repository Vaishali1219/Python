# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 12:46:23 2019

@author: vaish
"""
"""This function will comapre three numbers or strings and will return the status of their equality"""
def equal(a, b, c):
    if a==b or a==c or b==c:
        return True;
    else:
        return False;
"""First say Hii!!! :D"""
print('Hi!!!')
print("below is a function that can comapre strings and numbers and also can comapre numbers")
value=input("How many numbers you have to comapre: ")
if int(value)==3:
    """A function that compares only integers"""
    d =input("Enter the first number: ")
    e =input("Enter the second number: ")
    f =input("Enter the third number: ")
    print("The equality of two or more numbers you entered is ", equal(int(d), int(e), int(f)))
    ##break
elif int(value)==2:
     """A function that compares strings and integers"""
     d = '15'
     print('The first number by default is' + d)
     e =input("Enter the second number: ")
     f =input("Enter the third number: ")
     print("The equality of two or more numbers is ", equal(int(d), int(e), int(f)))
     ##break
else:
    print("U can call this function with either 2 or 3 values only")
    print("Come back again")
    ##break
"""Job Done so say Good Bye :D"""
print("Bye :D")



