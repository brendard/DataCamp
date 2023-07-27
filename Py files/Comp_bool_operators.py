# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 18:11:28 2023

@author: LENOVO
"""

""" Comparison operators. Pending: study how corrcoeff works"""

# Only elements of the same type can be compared, 
# except from integers and floats, or between numpy arrays,
# or between binaries (0,1) with False and True, respectively

# Code from Intro to Python for Data Science, chapter 4

import numpy as np
# np_height=np.array([1.73,1.68,1.71,1.89,1.79])
# np_weight=np.array([65.4,59.2,63.6,88.4,68.7])
# bmi=np_weight/np_height**2

# print(bmi>23)

# print(bmi[bmi>23])

# #print(bmi>21 and bmi<22)

# # ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

# # Use logical AND instead

# print(np.logical_and(bmi>21,bmi<22))
# print(bmi[np.logical_and(bmi>21,bmi<22)])

# # Comparing alphabetic order

# print("carl"<"chris")

# # Comparison of booleans
# print(True==False)

# # Comparison of integers
# print(-5*15!=75)

# # Comparison of strings
# print("pyscript"=="PyScript")

# # Compare a boolean with an integer
# print(True==1)

# # Comparison of integers
# x = -3 * 6
# print(x>=-10)

# # Comparison of strings
# y = "test"
# print("test"<=y)

# # Comparison of booleans
# True>False

# """ Compare arrays"""

# # Create arrays

# ## Bot arrays contain the areas of the kitchen, living room, bedroom and bathroom in the same order

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house>=18)

# my_house less than your_house
print(my_house<your_house)

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house>18.5,my_house<10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house<11,your_house<11))


