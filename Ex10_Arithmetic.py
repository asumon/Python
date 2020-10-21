# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:24:12 2020

@author: asumo
"""

'''
Exercise 10: Arithmetic
(Solved—20 Lines)
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of ab
Hint: You will probably find the log10 function in the math module helpful
for computing the second last item in the list.


'''
from math import log10

numberA=int(input("Enter your First Number :"))
numberB=int(input("Enter your second Number :"))

sum=numberA+numberB
difference=numberB-numberA
multi=numberA*numberB
quotient=numberA/numberB
remainder=numberA%numberB
result=log10(numberA)
power=numberA**numberB

print(f"The Summation of A & B is {sum}")
print(f"The difference of A & B is {difference}")
print(f"The Multiplication of A & B is {multi}")
print(f"The Division of A & B is {quotient}")
print(f"The Reminder of A & B is {remainder}")
print(f"The log10 result of A & B is {result}")
print(f"The power of A & B is {power}")