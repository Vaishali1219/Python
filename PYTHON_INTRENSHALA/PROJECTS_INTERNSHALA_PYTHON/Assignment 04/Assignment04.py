# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 21:14:31 2019

@author: vaish
"""
"""
This code has two classes 'book'  and 'ebook'

Class book =>

1) Constructors = __init__ and set_MyBook()
2) Accessors = get_MyBook() returns the result in the form of a dictionary
3) A royalty method for calculating royalty
4) class ebook inherits from class book and calls set_MyBook() method of book class for initialization
5) royalty() method of ebook class overrides the royalty() method of book class.

"""



#________________________________________________________________________________________________________________________________________________________________
class book:
    def __init__(self):
        self.title = 'My Book'
        self.author = 'Vaishali'
        self.publisher = 'Navneeth'
        self.price = 1219
        self.copies = 1
#----------------------------------------------------------------------------------------------------------------------------------------------------------
        
    def get_MyBook(self):
        MyBook = {'title': self.title, 'author': self.author, 'publisher': self.publisher, 'price':self.price, 'royalty': self.royalty()}
        for key in MyBook:
            print("{} => {}".format(key, MyBook[key]))
            print()
#----------------------------------------------------------------------------------------------------------------------------------------------------------
            
    
    def set_MyBook(self, t, a, p, pr, co):
        self.title = t
        self.author = a
        self.publisher = p
        self.price = pr
        self.copies = co
#----------------------------------------------------------------------------------------------------------------------------------------------------------
    def royalty(self):
        if self.copies < 500:
            royalty = 0.10 * self.price * self.copies
        elif self.copies > 500 and self.copies <= 1500:
            temp = 0.10 * self.price * 500
            royalty = (0.125 * self.price * (self.copies - 500)) + temp
        else:
            temp = 0.10 * self.price * 500
            t = 0.125 * self.price * 1000
            royalty = (0.15 * self.rice * (self.copies - 1500)) + temp + t
        return royalty
#________________________________________________________________________________________________________________________________________________________________                               
class ebook(book):
    def __init__(self):
        super().__init__()
        self.format = "pdf"
        
    def set_MyBook(self, t, a, p , pr, co, f = "pdf"):
        super().set_MyBook(t, a, p, pr, co)
        self.format = f
        
    def get_MyBook(self):
        MyBook = {'title': self.title, 'author': self.author, 'publisher': self.publisher, 'price':self.price, 'royalty': self.royalty(), 'format':self.format}
        for key in MyBook:
            print("{} => {}".format(key, MyBook[key]))
            print()
       
        
    def royalty(self):
        if self.copies < 500:
            royalty = (0.10 * self.price * self.copies) + (0.12 * self.price)
        elif self.copies > 500 and self.copies <= 1500:
            temp = 0.10 * self.price * 500
            royalty = (0.125 * self.price * (self.copies - 500)) + temp + (0.12 * self.price)
        else:
            temp = 0.10 * self.price * 500
            t = 0.125 * self.price * 1000
            royalty = (0.15 * self.rice * (self.copies - 1500)) + temp + t + (0.12 * self.price)
        return royalty
    
#________________________________________________________________________________________________________________________________________________________________                               

def decor(stri):
    length = len(stri)
    print("-" * length)
    print(stri)
    print("-" * length)
    print()
    return

b1 = book() #b1 is an obj of 'book' class and is initialized with default agrguments
decor("Details of Book b1-")
MyBuk = b1.get_MyBook()
print()
print()

b3 = book() #b3 is an obj of class 'book' and has values initized
b3.set_MyBook("MyPython", "Vaishali", "Navneeth", 10, 600)
decor("Details of Book b3-")
MyBuk = b3.get_MyBook()
print()
print()

b2 = ebook() #b2 is an obj of class 'ebook' and has values initized
b2.set_MyBook("AI", "Vaish", "Navi", 12, 700, "TXT")
decor("Details of ebook b2-")
MyBuk = b2.get_MyBook()
print()
print()

decor("Other Examples -")
ro = book.royalty(b1) 
print("Royalty of book 'b1' is {}\n" .format (ro))
ro = book.royalty(b3)
print("Royalty of book 'b3' is {}\n".format (ro))
print("Format of ebook 'b2' is {}\n".format (b2.format))
print()
print()

b4 = ebook()
decor("Details of ebook b4-")
MyBuk = b4.get_MyBook() #b4 is an obj of 'ebook' class and is initialized with default agrguments

#________________________________________________________________________________________________________________________________________________________________                               
   
    
    
        
    
