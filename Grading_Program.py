# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 23:50:38 2020

@author: asumon
"""

## DICTIONARY
# KEY : VALUE
# BUG : Value
# Function : Value
# Loop :    Value

student_scores= {
    "Zabid" : 81,
    "Rony" : 78,
    "Babu" : 99,
    "Lira" : 74,
    "Sumon" : 73,
    "Aziz" : 88,
    "Sohel" : 77,
    "Kajal" : 54,
        
    }

student_grades= {}

# Add the grades to student
for student in student_scores:
    score=student_scores[student]
    if score >90:
        student_grades[student]="Outstanding"
    elif score>80:
        student_grades[student] = "Exceeds Expections"
    elif score>70:
        student_grades[student]="Acceptable"
    else:
        student_grades[student] ='Fail'

print(student_grades)