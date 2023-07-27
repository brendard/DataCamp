# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 22:26:05 2023

@author: LENOVO
"""

""" if, elif, else"""

z=2

# print("checking "+str(z))
# if z%2==0:  # True (the colon indicates you have to indent expression to execute)
#     print("z is even") 
# else:
#     print("z is odd")
    
# To quit the if statement, you can keep on coding next without indentation

# print("checking "+str(z))
# if z%2==0:  
#     print("z is divisible by 2") 
# elif z%3==0: 
#     print("z is divisible by 3") 
# else:
#     print("z is neither divisible by 2 nor by 3")

# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15.0:
    print("big place!") #not printed because are is smaller
    
# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else:
    print("pretty small.")
    
# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else :
    print("pretty small.")
    
