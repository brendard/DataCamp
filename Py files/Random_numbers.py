# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 17:51:30 2023

@author: Brenda Rojas Delgado
"""
""" Create random generators """

# Setting the seed means that you are creating seed random numbers (ndarray type).
# If seed=12, generates 12 numbers, if seed=123, generates 123, and so on.
# If no seed is set up, only one random number is generated (float type)
# Calling twice random function generates different random numbers, with no seed at all or with the same seed

import numpy as np
# # Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

np.random.rand(123)                # Pseudo-random numbers
#print(np.random.rand())           # With no seed
# coin=np.random.randint(0,2)         # Randomly generates 0 or 1
# print(coin)
# if coin==0:
#     print("heads") 
# else:
#     print("tails")

# Use randint() to simulate a dice
# print(np.random.randint(1,7))

# # Use randint() again
# print(np.random.randint(1,7))

# # Starting step
# step = 50

# # Roll the dice
# dice=np.random.randint(1,7)

# # Finish the control construct
# if dice <= 2 :
#     step = step - 1
# elif dice<=5 :
#     step=step+1
# else :
#     step = step + np.random.randint(1,7)

# # Print out dice and step
# print(dice,step)

# """ New code: headtails.py (no random walk)"""

# outcomes=[]
# for x in range(10):
#     coin=np.random.randint(0,2)
#     if coin==0:
#         outcomes.append("heads") 
#     else:
#         outcomes.append("tails")
# print(outcomes)
    
""" headtails.py (random walk with coins)"""

# final_tails=[]
# for x in range(100000): # a 10-time toss repeated 100 times
#     tails=[0]
#     for x in range(10):
#         coin=np.random.randint(0,2)
#         tails.append(tails[x]+coin)
#     final_tails.append(tails[-1])
# #print(final_tails,tails)
# plt.hist(final_tails,bins=10)
# plt.show()

""" Random walk with dice """

# # Initialize random_walk
# random_walk=[0]

# # Complete the ___
# for x in range(100) :
#     # Set step: last element in random_walk
#     step=random_walk[-1]

#     # Roll the dice
#     dice = np.random.randint(1,7)

#     # Determine next step
#     if dice <= 2:
#         # Replace below: use max to make sure step can't go below 0
#         step = max(0,step - 1)
#     elif dice <= 5:
#         step = step + 1
#     else:
#         step = step + np.random.randint(1,7)

#     # append next_step to random_walk
#     random_walk.append(step)

# # Print random_walk
# print(random_walk)

# # Plot random_walk
# plt.plot(random_walk)  # Repeated, can plot several random lines

# # Show the plot
# plt.show()

""" All walks - Final exercise """

# clear the plot so it doesn't get cluttered if you run this many times
plt.clf()

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk five times
for i in range(500) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
# Implement clumsiness
        if np.random.rand()<=0.005 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)
#     # Append random_walk to all_walks
#     all_walks.append(random_walk)

# # Print all_walks
# print(all_walks)

# # Convert all_walks to NumPy array: np_aw
# np_aw=np.array(all_walks)

# # Plot np_aw and show
# plt.plot(np_aw)
# plt.show()

# # Clear the figure
# plt.clf()

# # Transpose np_aw: np_aw_t
# np_aw_t=np.transpose(np_aw)

# # Plot np_aw_t and show
# plt.plot(np_aw_t)
# plt.show()

# Create and plot np_aw_t with clumsiness
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)

# # Clear the figure
plt.clf()

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()