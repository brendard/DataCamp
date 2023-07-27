# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 21:12:24 2023

@author: Brenda Rojas Delgado
"""

""" Inner joins"""

import pandas as pd

# Open taxi_owners and taxi_veh .p files
taxi_owners = pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\taxi_owners.p')
taxi_vehs=pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\taxi_vehicles.p')

# Merge the taxi_owners df with taxi_veh df tables
taxi_own_veh = taxi_owners.merge(taxi_vehs,on='vid')

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_vehs, on='vid', suffixes=('_own','_veh'))

# Print the column names of taxi_own_veh
print(taxi_own_veh.columns)

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())

# Open ward and census .p files
ward = pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\ward.p')
census=pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\census.p')

# Merge the wards and census tables on the ward column
wards_census = ward.merge(census,on='ward')

# Print the shape of wards_census
print('wards_census table shape:', wards_census.shape)

# Merge the wards_altered and census tables on the ward column

# First, create these datasets

census_altered = census.copy()
census_altered.at[0,'ward']=None
print(census_altered.dtypes)

ward_altered = ward.copy()
ward_altered.at[0,'ward']=61
print(ward_altered.dtypes)

# Print the first few rows of the wards_altered table to view the change 
print(ward_altered[['ward']].head())

# Merge the wards_altered and census tables on the ward column
ward_altered_census = ward_altered.merge(census,on='ward')

# Print the shape of wards_altered_census
print('wards_altered_census table shape:', ward_altered_census.shape)

# Print the first few rows of the census_altered table to view the change 
print(census_altered[['ward']].head())

# Merge the wards and census_altered tables on the ward column
ward_census_altered = ward.merge(census_altered,on="ward")

# Print the shape of wards_census_altered
print('wards_census_altered table shape:', ward_census_altered.shape)

# Compare if the two tables are equal
print(ward_census_altered.equals(ward_altered_census))



""" Analyze this piece of code later to determine if you can merge tables after converting
an int64 column to object

# #ward_altered_census = ward_altered.merge(census,on='ward')
# # ValueError: You are trying to merge on int64 and object columns. If you wish to proceed you should use pd.concat

# # Check the types of ward in census_altered and ward_altered
# # print(ward_altered['ward'].dtype.name)
# # ward_altered['ward']=pd.to_datetime(ward_altered['ward'])
# print(ward_altered.dtypes)
# ward_altered["ward"] = ward_altered["ward"].astype(object)
# print(ward_altered.dtypes)
# print(census_altered.dtypes)

# ward_altered_census = ward_altered.merge(census,on='ward')

# census_altered.replace(to_replace = "None", value = 0, inplace=True)

# census_altered.iloc[0] = census_altered.iloc[0].astype(int)

# census_altered.iloc[:,0] = census_altered.iloc[:,0].astype(str)
# # census_altered.iloc[:,0] = census_altered.iloc[:,0].fillna(0)
# # print(census_altered.iloc[:,0])

# # Print the shape of wards_altered_census
# #print('wards_altered_census table shape:', ward_altered_census.shape)

#ward_altered_census = ward_altered.merge(census,on='ward')

"""

