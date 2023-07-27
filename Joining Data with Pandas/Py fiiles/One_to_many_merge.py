# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 17:28:59 2023

@author: Brenda Rojas Delgado
"""

import pandas as pd

# Open biz_owners and licenses .p files
biz_owners = pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\business_owners.p')
licenses=pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\licenses.p')

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on="account")

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby("title").agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values(by=['account'],ascending=[False])

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())


""" This is a separate code that will run once the dataset be found

# Merge the ridership and cal tables
ridership_cal = ridership.merge(cal)

# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
            				.merge(stations)

# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
							.merge(stations, on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7) 
                   & (ridership_cal_stations['day_type'] == 'Weekday') 
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo,on="zip") \
            			.merge(wards,on="ward") 

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby("alderman").agg({'income':'median'}))

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census,on="ward",suffixes=('_cen', '_lic'))\
.merge(licenses,on="ward",suffixes=('_cen', '_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'], 
                                   as_index=False).agg({'account':'count'})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(["vacant","account","pop_2010"], 
                                             ascending=[False,True,True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())

"""





