# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:13:59 2019

@author: vaish
"""
def getHint(a, k, v):
        if k in a and (a[k] == v):
            return True
        else:
            return False
    
def printMysong(a, t):
    print(t)
    print()
    for x in a:
        print(x,"-", a[x])
        print()
    return


YourSongDict = {}
MySongDict = {"Song": "Yeah", "Label":"Arsita","Duration":"4.10","Genre":"Pop", "PlayBack":"Jonathan Smith", "ReleaseYear":"2004"}
print("Now lets play a game.....Now guess and describe my Favourite song...:D")
print()
choice = input("Are you ready????: ")
if choice == "Yes" or choice == "yes":
    print()
    Title = "DESCRIPTION OF MY FAVOURITE SONG"
    Find = False
    while(Find == False):
        key = input("Now guess any one attribute of my favourite song...: ")
        print()
        val = input("Guess the attribute name: ")
        Find = getHint(MySongDict, key, val)
        if Find == False:
            print("Opps Try once again!!")
    
    if Find == True:
        print()
        print(Find)
        print("U got it :D")
        print()
    
    print("here is my fav song:D")
    print()
    printMysong(MySongDict, Title)

