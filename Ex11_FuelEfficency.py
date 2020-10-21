# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 01:32:16 2020

@author: asumo
"""

'''
Exercise 11: Fuel Efficiency
(13 Lines)
In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.



'''
ltm =235.21
usaunit=int(input("Enter the fuel unit in USA standard :"))

canada_ltr_per_kl=ltm/usaunit

print(f"The Fuel efficiency of canadian unit {canada_ltr_per_kl} is equiavalent of USA mpg {usaunit} : ")
