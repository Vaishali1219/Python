# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:51:10 2019

@author: vaish
"""

"""ABSTRACT: This program will print numbers in the range 1 to 100. First it checks out whether the number is divisible by 3/5 or it is prime. If the
number is divisible by 3 will print Fizz or if it is divisible by 5 will print Buzz or if by both will print FizzBuzz. If the number is prime will print prime.

Step 1: Print all numbers in the range 1 to 100
Step 2: Get the user input to check whether the user needs only codes or Number + codes
Step 3: Check all the numbers and set the correspondings flags as applicable.
Step 4: As per the user's wish print the output.

VARIABLES USED IN THE PROGRAM:
1)  num = [] This will have elements numbers with Codes
2) numbers = [] This will have elements only codes of the numbers
3) pattern and f: decalred for formating the output
    
FUNCTIONS USED IN THE PROGRAM:
1) checkPrime : Checks if the number is prime
2) checkMod3 : Checks if the number is divisible by 3
3) checkMod5 : Checks if the number is divisible by 5
4) checkNum : To determine the code of the number
5) PrintList : To print the elemnts of numbers list
6) PrintMyList : To print the elemts of num list
7) checkFlags : This for checking out the flags set to determine the format of printing
    
The purpose of adding too many functions is that ONLY A MAXIMUM OF 10 NUMBERS WILL BE PRINTED IN A SINGLE ROW IN A PARTICULAR FORMAT"""

"""Function to check whether the number is Prime or Composite"""
def checkPrime(n):
    Flag = 0
    for x in range(2, n): #This statement checks if the number is divisible by 2 to n-1
        if (n % x) == 0:
            Flag = 1 #If the number is composite the Flag will be set to 1
            break
    return (Flag) #This function will return eiher 0 ot 1
        
"""Function to check whether the number is divisible by 3"""
def checkMod3(m):
        if (m % 3) == 0: #This statement will check if the number is divisible by 3 and return 1 or will return 0
            return 1
        else:
            return 0        

"""Function to check if the number the divisible by 5"""
def checkMod5(m):
        if (m % 5) == 0: #This statement will check if the number is divisible by 5 and return 1 or will return 0
            return 1
        else:
            return 0
        
"""Function to get the code for the given number"""    
def checkNum(n):    #All the numbers will be checked out in the functions below and the corresponding Flags will be set
    primeFlag = checkPrime(n)
    mod3Flag = checkMod3(n)
    mod5Flag = checkMod5(n)
     #This function will return a numbers code
    if ((mod3Flag == 1) and (mod5Flag == 1)):
        if primeFlag == 0:
            return('FizzBuzz and Prime')
        else:
            return('FizzBuzz')
        return
 
    elif (mod3Flag == 1):
        if primeFlag == 0:
            return('Fizz and Prime')
        else:
            return('Fizz')
    
    elif (mod5Flag == 1):
        if primeFlag == 0:
            return("Buzz and Prime")
        else:
            return('Buzz')
    else:
        if primeFlag == 0:
            return('Prime')
        else:
            return(n)
            
"""Function to print the series only with codes"""
def PrintList(b = []):
     print(b[0],' ' * 15,end='')
     for j in range(1, 100):
         if b[j] == 'Fizz and Prime':
             print(b[j],' ' * 3,end='')
         elif b[j] == 'FizzBuzz':
             print(b[j],' ' * 9,end='')
         elif b[j] == 'Prime':
             print(b[j],' ' * 12,end='')
         elif b[j] == 'Fizz':
             print(b[j],' ' * 13,end='')
         elif b[j] == 'Buzz':
             print(b[j],' ' * 13,end='')
         else:
             print(b[j],' ' * 15,end='')
         if j % 10 == 9:
             print("\n")
             print()
            
                
"""Function to print the series in given format"""  
def PrintMyList(a = []):
        print(a[0],' ' * 20,end='')
        for j in range(1, 100):
         if 'Fizz and Prime' in a[j]:
             print(a[j],' ' * 3,end='')
         elif 'FizzBuzz' in a[j]:
             print(a[j],' ' * 7,end='')
         elif 'Prime' in a[j]:
             print(a[j],' ' * 10,end='')
         elif 'Fizz' in a[j]:
             print(a[j],' ' * 11,end='')
         elif 'Buzz' in a[j]:
             print(a[j],' ' * 11,end='')
         else:
             print(a[j],' ' * 20,end='')
         if j % 10 == 9:
             print("\n")
             print()
                
"""This function is to check out which flag is set"""           
def checkFlags(a):
    if a in ('Prime','Buzz',"Buzz and Prime", 'Fizz','Fizz and Prime','FizzBuzz','FizzBuzz and Prime'):
        return 1
    else:
        return 0

"""This is the main Function"""
def main():
    pattren = ''
    num = []
    numbers = []
    f = 0
    print('\n')
    print('\n')
    print('\n')
    print("This program will print Fizz for a number divisible by 3 and")
    print("will print Buzz for a number divisible by 5 and")
    print("will print FizzBuzz for a number divisible by both 3 and 5")
    print("And Finally Will print Prime for a prime number")
    print('\n')
    print('\nThe below codes will display numbers from 1 to 100')
    print('\n')
    for x in range(1, 101):
        print(x,'\t',end='')
        if x % 10 == 0:
            print()
    print('\n')
    print('\n')
    print('\n')
    print("How you want to display the result")
    print("Wether you wanna display only code or number with code")
    print("1> For displaying only Code enter 'C'")
    print("2> For displaying Code with Numbers enter 'N'")
    print("\n")
    c = input("Enter your code: ")
    print('\n')
    print('\n')
    print('\n')
    for j in range(1,101):
        if j == 1:
            num.append(j)
            numbers.append(j)
            continue
        elif j==2:
            num.append('2 = Prime')
            numbers.append('Prime')
            continue
        else:
            code = checkNum(j)
            numbers.append(code) #The numbers code will be added to numbers list
            f = checkFlags(code)
            if f == 0: # If none of the flags are set only the number will be set else the number will be displayed in the given format
                pattren = "%d" % (j)
            else:
                pattren = "%d = %s" % (j, code)
        
            num.append(pattren)
    if (c == 'N' or c == 'n'):
        PrintMyList(num)
    elif (c == 'C' or c == 'c'):
        PrintList(numbers)
    else:
        print("Sorry Invalid code reboot")
        quit()
        
main()