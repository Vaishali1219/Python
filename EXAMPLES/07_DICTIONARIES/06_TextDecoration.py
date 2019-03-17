# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 15:07:30 2019

@author: vaish
"""

def decor(func, fun):
    def wrap():
        length = len("{}".format(func()))
        print("=" * length)
        fun()
        print("=" * length)
    return wrap

def print_text():
    print("Hello")
    
def len_text():
    return("Hello")

decorated = decor(len_text, print_text)
decorated()