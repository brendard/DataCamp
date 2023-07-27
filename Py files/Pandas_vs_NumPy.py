# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:38:54 2023

@author: LENOVO
"""

""" Pandas vs NumPy examples"""

# Pandas is built on NumPy

import pandas as pd
import numpy as np

#Creating the BRICS dataset manually

# BRICS_dict={"country":["Brazil","Russia","India","China","South Africa"],
#             "capital":["Brasilia","Moscow","New Delhi","Beijing","Pretoria"],
#             "area":[8.516,17.10,3.286,9.597,1.221],
#             "population":[200.4,143.5,1252,1357,52.98]}

# brics=pd.DataFrame(BRICS_dict)

# brics.index=["BR","RU","IN","CH","SA"]

# print(type(brics[["country"]]))

# print(brics[["country","capital"]]) # To select certain cloumns
# print(brics[1:4])  # To select certain rows

# """ Filtering pandas dataframe: BRICS"""

# #brics_area=brics['area'] # as series or
# #brics_area=brics.loc[:,'area']
# #brics_area=brics.iloc[:,2]

# is_huge=brics["area"]>8
# #print(brics[is_huge]) #or
# print(brics[brics["area"]>8])

# # Now let's operate with logical operators (NumPy)

# print(brics[np.logical_and(brics["area"]>8,brics["area"]<10)])

## Open brics as csv

# brics_csv=pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Intermediate Python/brics.csv",index_col=0)
# print(brics_csv)

# Creating a dict assigned as variables

# Pre-defined lists
# names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
# dr =  [True, False, False, False, True, True, True]
# cpc = [809, 731, 588, 18, 200, 70, 45]

# # Create dictionary my_dict with three key:value pairs: my_dict
# cars_dict={'country':names,'drives_right':dr,'cars_per_cap':cpc}

# # Build a DataFrame cars from my_dict: cars
# cars=pd.DataFrame(cars_dict)

# # Print cars
# print(cars)

# # Definition of row_labels
# row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# # Specify row labels of cars
# cars.index=row_labels

# # Print cars again
# print(cars)

# Now redo the procedure with the csv file

cars_csv = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Intermediate Python/cars.csv",index_col=0)
print(cars_csv)

cars=cars_csv.reset_index(drop=True) # Pending of index removal and rename the first column

cars=cars.rename(index={0:'US',1:'AUS',2:'JPN',3:'IN',4:'RU',5:'MOR',6:'EG'})
#del cars['Unnamed: 0']

# Indexes are never counted as rows or columns

columns_titles = ["country","cars_per_cap","drives_right"]
cars=cars.reindex(columns=columns_titles)

cars["name_length"] = cars["country"].apply(len)
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Iterate over rows of cars
# for lab,row in cars.iterrows():
#     # print(lab) 
#     # print(row) 
#     #cars.loc[lab, "name_length"] = len(row["country"]) #apply is a better method. because you are not creating a new dataseries with each iteration
#     #cars.loc[lab, "COUNTRY"] = row["country"].upper()
#     print(lab + ": " + str(row['cars_per_cap']))

#cars.insert(1,"Capital",['Washington','Camberra','Tokyo','New Delhi','Moscow','Rabat','Cairo'],True)

print(cars)

""" Begin to reaccomodate this code to make it work"""

# print(type(cars[["country"]]) # accomodate this code line where it goes

# """loc (label-based) and iloc (integer position-based)"""

# """ loc access"""

# # loc allows accesing rows and columns at the same time with labels
# # Without the loc, rows are accesed only throug numeric slicing

# cars_ru=brics.loc["RU"]    # shown as series
# cars_ru2=brics.loc[["RU"]] # shown as dataframe

# cars_3=brics.loc[["RU","IN","CH"],["country","capital"]] # Selection extended with a comma
# cars_4=brics.loc[:,["country","capital"]] # Selection of all rows and two columns

# """iloc access"""

# cars_ru2=brics.iloc[[1]] 
# cars_3=brics.iloc[[1,2,3],[0,1]]  # it works exactly like matrices in Matlab

# cars_4=brics.iloc[:,[0,1]]

# """ DataCamp Pandas exercises without loc and iloc"""

# # Print out country column as Pandas Series
# print(cars['country'])

# # Print out country column as Pandas DataFrame
# print(cars[['country']])

# # Print out DataFrame with country and drives_right columns
# print(cars[['country','drives_right']])

# # Print out first 3 observations
# print(cars[0:3])  # We are selecting based on integer indexes, not row labels

# # Print out fourth, fifth and sixth observation
# print(cars[3:6])  

# # Print out observation for Japan
# print(cars.loc['JPN'])

# # Print out observations for Australia and Egypt
# print(cars.iloc[[1,6]])

# # Print out drives_right value of Morocco
# print(cars.loc['MOR', 'drives_right'])

# # Print sub-DataFrame
# print(cars.loc[['RU','MOR'], ['country','drives_right']])

# # Print out drives_right column as Series
# print(cars.loc[:,"drives_right"])

# # Print out drives_right column as DataFrame
# print(cars.iloc[:,[2]])

# # Print out cars_per_cap and drives_right as DataFrame
# print(cars.loc[:,['cars_per_cap','drives_right']])

# """Other examples with loc and iloc"""
# cars.loc['IN', 'cars_per_cap']
# cars.iloc[3, 0]

# cars.loc[['IN', 'RU'], 'cars_per_cap']
# cars.iloc[[3, 4], 0]

# cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
# cars.iloc[[3, 4], [0, 1]]

# """ Exercise of the chapter"""

# # Extract drives_right column as Series: dr
# dr=cars['drives_right']

# # Use dr to subset cars: sel
# sel=cars[dr]

# # Print sel
# print(sel) 

# # Convert code to a one-liner
# sel = cars[cars['drives_right']]

# # Print sel
# print(sel)

# # Create car_maniac: observations that have a cars_per_cap over 500
# cpc=cars["cars_per_cap"]>500
# car_maniac=cars[cpc]

# # Print car_maniac
# print(car_maniac)

# # Create medium: observations with cars_per_cap between 100 and 500
# medium=cars[np.logical_and(cars["cars_per_cap"]>100,cars["cars_per_cap"]<500)]

# # Print medium
# print(medium)