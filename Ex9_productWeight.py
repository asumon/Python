# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:10:38 2020

@author: asumo
"""

widget=0.75
gizmo=0.112

widget_order=int(input("How many order of Widget :"))
gizmo_order=int(input("How many order of Gizmo :"))
total_weight=widget*widget_order + gizmo*gizmo_order
print(f"Total weight {total_weight} of the order given by the user")
