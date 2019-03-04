# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 21:34:22 2019

@author: vaish
"""
"""These line of codes is to check the availability of UserName """

myUniqueList = ['vaish19', 'hi5', 'Navi12', 'Win10', 'Bannana100'] #a predefined list with some value
myLeftovers = [] ##An Empty list to append rejected ones

def addleft(y):  ## A function to add Rejeceted ones
    myLeftovers.append(y)
    return

def checkAvailability(z): ## This function receives UserName as a parameter
        if not z in myUniqueList: ## If UserName is not in the list the name will be appeneded and the function returns TRUE else will return False
                myUniqueList.append(z)
                return True        
        else:
            return False
        
def checkValid(x): ##This function will receive UserName as Parameter
    if (x[0]=='_' or ord(x[0]) in range(65,90) or ord(x[0]) in range(97,122)): ## checks wheter the first letter is _/a to z/A to Z and retuens TRUE if true else FALSE
        return True
    else:
        return False
    
print("RULES TO BE FOLLOWED: ") ## The below code would print the rules to be followed
print("1. User name can begin with Capital (A)/ small (a) / UnderScore (_)")
print("2. User name should not begin with numbers or symbols")
print("3. User name can be a mixture of symbol of letters and symbols")
UserName =input("Enter the your desired User Name: ") ## Get an user input
Validity = checkValid(UserName) ## Check wheter the UserName compy the rules so checkValid() function is called
if Validity==True: ## if Validity is TRUE the follwing codes will be executed
    print("User Name is valid carry on")
    status = checkAvailability(UserName)
    if status==True:
        print("Your UserName is valid and is AVAIALABLE")
        print(myUniqueList)
    else:
        addleft(UserName)
        print('The UserName is NOT available')
        print(myLeftovers)
else:
    addleft(UserName) ## Even the invalid names are sent to lefover list
    print(myLeftovers)
    print("Your User Name doesnot comply the rules please try again")
    

