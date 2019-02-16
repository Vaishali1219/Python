# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:24:31 2019

@author: vaish
"""

n1 = input("Binary n1: ")
n2 = input("Binary n2: ")

"""Strings n1 and n2 are converted to decimals since bitwise operations can be performed only with numbers. While the binary
representation of the number is a string"""

n1 = int(n1, 2)
n2 = int(n2, 2)

"""In Computer memory binary operations are performed on bits of numbers. althjough we specify decimals as operands. Also the result
is also a decimal number"""

bit_or = bin(n1 | n2)
bit_and = bin(n1 & n2)
bit_xor = bin(n1 ^ n2)

"""The bin of function converts decimal number to binary, which is a string, the first two characters are '0b'"""

print("n1: %10s" % bin(n1))
print("n2: %10s" % bin(n2))
print("-------------------")
print("OR: %10s" % bit_or)
print("AND: %10s" % bit_and)
print("XOR: %10s" % bit_xor)



