# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 15:54:52 2023

@author: LENOVO
"""

"""Dictionaries"""

# Data analysis with indexes (no dict)
# pop=[30.55,2.77,39.21]
# countries=["afghanistan","albania","algeria"]

# ind_alb=countries.index("albania")

# print(ind_alb)

# print(pop[ind_alb])

# Data analysis with dicts (no indexes)

# world={"afghanistan":30.55,"albania":2.77,"algeria":39.21}
# print(world["albania"])

# # Add element to an existing dictionary
# world["sealand"]=0.000027

# print("sealand" in world)
# world["sealand"]=0.000028

# # Delete element to an existing dictionary
# del(world["sealand"])
# print(world)

# # Definition of countries and capital
# countries = ['spain', 'france', 'germany', 'norway']
# capitals = ['madrid', 'paris', 'berlin', 'oslo']

# # With index method
# ind_ger=countries.index("germany")
# print(ind_ger)

# # Use ind_ger to print out capital of Germany
# print(capitals[ind_ger])

# # With dict method

# # From string in countries and capitals, create dictionary europe
# europe = {'spain':'madrid','france':'paris', 'germany':'berlin', 'norway':'oslo' }

# # Add italy to europe
# europe['italy']='rome'

# # Print out italy in europe
# print('italy' in europe) # it prints out if the value is really there

# # Add poland to europe
# europe['poland']='warsaw'

# # Print out the keys in europe
# print(europe.keys())

# # Print out value that belongs to key 'norway' and 'poland'
# print(europe['norway'],europe['poland'])

# # Delete an element from Europe

# del(europe['norway'])

# Let's reformulate europe to include other lists inside

""" Dictionary of dictionaries """

europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data={ 'capital':'rome', 'population':59.83 }

# Add data to europe under key 'italy'
europe['italy']=data

# Print europe
print(europe)

