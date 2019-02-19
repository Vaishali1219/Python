# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:37:57 2019

@author: vaish
"""

extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']
fname = input("Enter file name: ").split('.') #Splits a string name after a dot

if len(fname) >= 2:
    fname_ext = fname[-1].lower()
    if fname_ext in extensions:
        print("Yes")
    else:
        print("No")
else:
    print("The fname has no extension")
    