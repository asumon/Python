# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 03:37:15 2020

@author: asumon
"""


def prime_checker(number):
    is_prime=True
    for j in range(2,number-1):
        if number % j == 0:
           is_prime=False
    if is_prime:
        print(f"{number} is a Prime number :")
    else:
        print(f"{number} is Not a prime number")
    
number=int(input("Enter the decimal number : "))
prime_checker(number)



