# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:13:59 2019

@author: vaish

Python Is Easy: Assignment #7: Dictionaries and Sets

Details:
 
Return to your first homework assignments, when you described your favorite song. 
Refactor that code so all the variables are held as dictionary keys and value. 
Then refactor your print statements so that it's a single loop that passes through each item in the dictionary 
and prints out it's key and then it's value.


Extra Credit:

Create a function that allows someone to guess the value of any key in the dictionary, 
and find out if they were right or wrong. This function should accept two parameters: Key and Value. 
If the key exists in the dictionary and that value is the correct value, then the function should return true. 
In all other cases, it should return false.

Methods:
    
1> getKey() - This method is to let user select the Key for which she/he wants to guess the value and returns the key

2> GuessMySong(a, k, v) - This function is to check whether the user guess right or not. This function takes in three parameters:
       a) a - The dictionary 
       b) k - key
       c) v - value
    and this will return either True or False:
        True: If guessed right
        False: If the value entered was wrong
        
3> GetDict() - This function decalares a varaiable of type dictionary and returns the same.

4> GetDictlen() - This function will return a String data type which is the title of the game.

5> printMysong() - This function doesn't return anything but it is for printing the entire dictionary

6> decor(func, fun) - This function is for printing text decoration around the output. This takes in two parameters and both are functions.
       a) Func - To get the length untill which the decoraters have to be wrapped around
       b) Fun - This Function will print the actual text

Variables:
    
I) main():
    
1> Res - This is a boolean data type and is initially set to False so that untill the user guesses the corrrect value the program will loop

2> MySongDict - This is a dictionary datatype and will hold the value of the dictionary in main function

3> choice - This is a string datatype and will get the user input to whether to continue or not

4> Key = Hold the key value; String Datatype

6> Val = String; Holds the user input value for the key

II) getKey():
    
1> Find - This is a boolean datatype and is set to False initially

2> val - int data type and gets assigned the user input value

3> Fkey - Holds the corresponding actual key value

III) GetDict():

1> D - Dictionary Datatype

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def decor(func, fun):
    def wrap():
        length = len("{}".format(func()))
        print("=" * length)
        fun()
        print("=" * length)
    return wrap
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

def GuessMySong(a, k, v):
        if k in a and (a[k] == v):
            return True
        else:
            return False

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
  
def printMysong():
    print(GetDictlen())
    print()
    a = GetDict()
    for x in a:
        print(x,"-", a[x])
        print()
    return

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

def GetDictlen():
    Title = "DESCRIPTION OF MY FAVOURITE SONG"
    return Title
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

def GetDict():
    D = {"Song": "Yeah", 
         "Label":"Arsita",
         "Duration":"4.10",
         "Genre":"Pop", 
         "PlayBack":"Jonathan Smith", 
         "ReleaseYear":"2004"}
    return D

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def getKey():
    Find = False
    while(Find == False):
        print("Now which attribute you can guess any one attribute of my favourite song...: ")
        print()
        print("1. Song\n2. Label\n3. Duration\n4. Genre\n5. PlayBack\n6. ReleaseYear\n")
        val = int(input("Enter your Option: "))
        if val == 1:
            Fkey = "Song"
            Find = True
            return Fkey
        
        elif val == 2:
            Fkey = "Label"
            Find = True
            return Fkey
        
        elif val == 3:
            Fkey = "Duration"
            Find = True
            return Fkey
        
        elif val == 4:
            Fkey = "Genre"
            Find = True
            return Fkey
        
        elif val == 5:
            Fkey == "PlayBack"
            Find = True
            return Fkey
        
        elif val == 6:
            Fkey = "ReleaseYear"
            Find = True
            return Fkey
        
        else:
            print("Please reenter value")
            Find = False
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    Res = False
    MySongDict = GetDict()
    print("Now lets play a game.....Now guess my Favourite song...:D")
    print()
    choice = input("Are you ready????: ")
    if choice == "Yes" or choice == "yes":
        while (Res == False):
            print()
            Key = getKey()
            Val = input("Now guess the {}: ".format(Key.capitalize()))
            Res = GuessMySong(MySongDict, Key, Val)
            if Res == True:
                print()
                print(Res)
                print("U got it :D")
                print()
                print("here is my fav song:D")
                print()
                printsong = decor(GetDictlen, printMysong)
                printsong()
            else:
                print("Opps Try once again!!")
                print()
    else:
        quit()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
    
main()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
"""    
ALGORITHIM:-

Step 1: mian()
   1> Set Res = False
   2> Get Dictionary
   3> Introduce to user
   4> Get the user response to continue or quit ("Through first if and else statemet")
   5> The program will loop through until the Res is False
      a) Get the key value the user wants to guess
      b) Get the value of the Key guessed by the user
      c) Check for the Res call GuessMySong function
    6> If Res is true the Dictionary will be printes
    7> Else the program will quit
"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
