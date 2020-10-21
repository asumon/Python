# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 01:50:54 2020

@author: asumo
"""

'''
Exercise 12: Distance Between Two Points on Earth
(27 Lines)
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
The value 6371.01 in the previous equation wasn’t selected at random. It is
the average radius of the Earth in kilometers.
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.



Hint: Python’s trigonometric functions operate in radians. As a result, you will
need to convert the user’s input from degrees to radians before computing the
distance with the formula discussed previously. The math module contains a
function named radians which converts from degrees to radians.
'''

import math
from math import radians
import numpy
pi=3.14

radius_earth=6371.01

t1=float(input("Enter the latitude of the first location:"))
t1=t1*(pi/180)
g1=float(input("Enter the longitude of the first location:"))
g1=g1*(pi/180)
t2=float(input("Enter the latitude of the Second location:"))
t2=t2*(pi/180)
g2=float(input("Enter the longitude of the Second location:"))
g2=g2*(pi/180)


#distance =radius_earth * arccos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 − g2))

dist = 6371.01 * arccos(sin(t1)*sin(t2) + cos(t1)*cos(t2)*cos(g2 - g1))

print(distance)
