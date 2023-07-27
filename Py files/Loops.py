# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 20:51:10 2023

@author: Brenda Rojas Delgado
"""

# error=50.0
# while error>1:
#     error=error/4 # Commented expressions give infinite loops
#     print(error)

""" Example of an inverted pendulum with while loop"""

# Initialize offset
#offset=-6  # if offset is negative, the loop will never stop running, unless an if-else statement is incorporated

# # Code the while loop
# while offset!=0:
#     print("correcting...")
#     offset=offset-1
#     print(offset)

# Code the while loop
# while offset != 0 :
#     print("correcting...")
#     if offset>0 :
#       offset = offset - 1
#     else : 
#       offset = offset + 1    
#     print(offset)

""" Example with for loop (they operate not only with strings and floats, but also list, etc."""

## for var in seq:   # var (arbitrary name) is automatically assigned when written here
#     # expression

# fam=[1.73,1.68,1.71,1.89]
# print(fam)

# for index, height in enumerate(fam):
#     print("index "+str(index)+ ": "+str(height))
    
# for c in "family":
#     print(c.capitalize())

# # Exercises from course

# # areas list
# areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# # Code the for loop
# for dim in areas:
#     print(dim)
    
# # Change for loop to use enumerate() and update print()
# for i, a in enumerate(areas) :
#     print("room "+str(i+1)+": "+str(a))
    
# # house list of lists
# house = [["hallway", 11.25], 
#          ["kitchen", 18.0], 
#          ["living room", 20.0], 
#          ["bedroom", 10.75], 
#          ["bathroom", 9.50]]
         
# # Build a for loop from scratch
# for index, area in enumerate(house):
#     print("the "+str(house[index][0])+" is "+str( house[index][1])+" sqm")

# """ Loop Data Structures Part 1"""
# """ Dictionaries"""
# # Bear in mind that dictionaries are inherintly unordered in Python 3 and before

# world={"afghanistan":30.55,
#        "albania":2.77,
#        "algeria":39.21}
# for key, value in world.items():
#     print(key+" -- "+str(value))

# """ NumPy arrays"""

# import numpy as np
# import pandas as pd

# np_height=np.array([1.73,1.68,1.71,1.89,1.79])
# np_weight=np.array([65.4,59.2,63.6,88.4,68.7])
# bmi=np_weight/np_height**2
# meas=np.array([np_height,np_weight]) # 2D NumPy array

# for val in meas:  # or bmi. It works the same
#     print(val)
    
# for val in np.nditer(meas):  # prints out each array iteratively
#     print(val)

# """ Exercises from DataCamp"""

# # Definition of dictionary
# europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
#           'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# # Iterate over europe
# for key,value in europe.items():
#     print("the capital of "+key+" is "+value)
    
# # For loop over np_height
# for height in np_height:
#     print(str(height)+" inches")

# np_baseball=pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Intermediate Python/np_baseball.csv",index_col=0)
# print(np_baseball)
# # For loop over np_baseball (find out how to print the head)
# for bsb in np.nditer(np_baseball,flags=["refs_ok"]):
#     print(bsb) #check out this code (the explanation might come next)
    
# Original code in DataCamp

# # For loop over np_baseball
# for bsb in np.nditer(np_baseball):
#     print(bsb)

""" Dataframes"""

# ## Open brics as csv

import pandas as pd
brics_csv=pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Intermediate Python/brics.csv",index_col=0)

'With for loop'

# for lab,row in brics_csv.iterrows():
     #print(lab,row)
     # print(lab)
     # print(row)
     #print(lab+" : "+row["capital"]) # - only saves the last iteration on Variables Explorer
     # - Creating series on every iteration
#      brics_csv.loc[lab,"name_length"] = len(row["country"])
# print(brics_csv)

'Without for loop and apply calls'

brics_csv["name_length"]=brics_csv["country"].apply(len)
print(brics_csv)

""" More about loops over dataframes"""



