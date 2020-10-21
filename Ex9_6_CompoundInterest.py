# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:58:12 2020

@author: asumo
"""

'''
Exercise 9: Compound Interest
(19 Lines)
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.

'''


interest_rate=4
deposited=float(input("Enter the deposited amount:"))
years=int(input("How many years your amount is deposited :"))

# p is principle amount, n is number of years and R is rate

pnr=deposited*years*interest_rate
simple_interest=pnr/100
total_amount=deposited+simple_interest

print(f'Your deposited amount is {deposited} for {years} Years with Interest rate {interest_rate} Percent and Total Amount Now :{total_amount}')
