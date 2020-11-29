# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 03:18:58 2020

@author: asumon
"""


import math

'''

wall_height=int(input("Enter the Height of the Wall :"))
wall_width=int(input("Enter the Width of the Wall :"))

area_of_the_wall=wall_height*wall_width
coverage_per_can=5

number_of_cans=(wall_height*wall_width)/coverage_per_can

number_of_cans=round(number_of_cans)

print(f"You will need {number_of_cans} cans for the area {area_of_the_wall} !!")

'''


def paint_calc(height,width,cover):
    area=height*width
    cans=area/cover
    cans=math.ceil(cans)
    print(f"You will need {cans} cans for the area {area} !!")
    
    
    
    
height=int(input("Enter the Height of the Wall :"))
width=int(input("Enter the Width of the Wall :"))
cover=int(input("Enter the number of cover :"))


paint_calc(height, width, cover)

    