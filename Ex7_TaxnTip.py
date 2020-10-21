# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:58:13 2020

@author: asumo
"""
tax_rate=0.25
tip_rate=0.16
cost=float(input("Enter the meals cost:"))
tax=cost*tax_rate
tip=cost*tip_rate
total=cost+tax+tip
print("The Tax is %.2f and the tip is %.2f, making the total meal cost %.2f" %(tax,tip,total))