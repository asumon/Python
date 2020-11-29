# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 00:26:24 2020

@author: asumon
"""

#Nesting



#Nesting a list in a Dictionary

travel_log = [{
    "country":"France", 
    "cities": ["Paris","Lille","Dijon"],
    "visits": 12,
    },
{
     "country":"Germany", 
    "cities": ["Berlin", "Hamburg","Stuttgart"],
    "visits": 5,
 }
    ]
        
    
def add_new_country(country_visited,times_visited,cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["visits"]=times_visited
    new_country["cities"]=cities_visited
    travel_log.append(new_country)
    
    
    



add_new_country("Bangladesh",3,["Dhaka","Comilla","Chittagong","CoxsBazar"])

print(travel_log)