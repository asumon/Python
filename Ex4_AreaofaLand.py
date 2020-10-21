# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:41:00 2020

@author: asumo
"""

sqft_per_acre=43560

width=float(input("Enter the width of the field in Feet:"))
length=float(input("Enter the length of the field in Feet:"))
acres=width*length/sqft_per_acre
print(f'The area of the field is {acres} acres')