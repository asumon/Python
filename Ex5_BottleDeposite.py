# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:41:00 2020

@author: asumo
"""

less_deposite=0.10
more_deposite=0.25
less=int(input("How many containers 1 litre or less do you have :"))
more=int(input("How many containers more than 1 litre do you have :"))
refund=less*less_deposite+more*more_deposite
print('Your total refund will be: $%.2f.' %refund)