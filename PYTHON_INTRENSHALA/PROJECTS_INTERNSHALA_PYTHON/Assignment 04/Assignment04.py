# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 21:14:31 2019

@author: vaish
"""

class book:
    def __init__(self, t='My Book', a='Vaishali', p='Navneeth', pr = 1219, co = 0):
        self._title = t
        self._author = a
        self._publisher = p
        self._price = pr
        self._copies = co
        
    def get_MyBook(self):
        MyBook = {'title': self._title, 'author': self._author, 'publisher': self._publisher, 'price':self._price, 'royalty': self.royalty(self._price, self._copies)}
        print(MyBook.items())
            
    
    def set_MyBook(self, t, a, p, pr, co):
        self._title = t
        self._author = a
        self._publisher = p
        self._price = pr
        self._copies = co
    
    @classmethod
    def royalty(self, price, copies):
        if copies < 500:
            royalty = 0.10 * price * copies
        elif copies > 500 and copies <= 1500:
            temp = 0.10 * price * 500
            royalty = (0.125 * price * (copies - 500)) + temp
        else:
            temp = 0.10 * price * 500
            t = 0.125 * price * 1000
            royalty = (0.15 * price * (copies - 1500)) + temp + t
        return royalty
                               
    MyBook = property(get_MyBook, set_MyBook)
       

b1 = book()
b1.set_MyBook("MyPython", "Vaishali", "Navneeth", 10, 600)
MyBuk = b1.MyBook

   
    
    
        
    
