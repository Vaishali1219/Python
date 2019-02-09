# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:13:01 2019

@author: vaish
"""

Participants = ["Jen", "Alex", "Tina", "Joe", "Ben"]
position = 0
for name in Participants:
    if name == "Ben":
        print("About to break")
        break
    print("About to increment")
    position += 1
print(position)

for currentIndex in range(len(Participants)):
    if Participants[currentIndex] == "Joe":
        print("Have breaked")
        break
print('not breaked')
print(currentIndex)
for number in range(10):
    if number % 3 == 0:
        print(number)
        print("Number divisible by 3")
        continue
    print(number)
    print("not divisible by 3")