# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 22:00:55 2023

@author: Brenda Rojas Delgado
"""

""" Filtering joins"""

import pandas as pd
import matplotlib.pyplot as plt

# open employees and top customers csv files
employees = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/employees.csv",encoding= 'unicode_escape',delimiter=';')
top_cust = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/top_cust.csv",encoding= 'unicode_escape',delimiter=';')

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on="srid", how="left", indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees["srid"].isin(srid_list)])

# open non_mus_tcks, top_invoices and genres csv files

non_mus_tcks = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/non_mus_tcks.csv",encoding= 'unicode_escape',delimiter=';')
top_invoices = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/top_invoices.csv",encoding= 'unicode_escape',delimiter=';')
genres = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/genres.csv",encoding= 'unicode_escape',delimiter=';')

# Merge the non_mus_tck and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices,on="tid",how="inner")

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres,on='gid'))

""" Concats"""

# When the dataframes are short enough, it is more convenient creating them from the scratch
# From larger files, read through csv, pickle formats, and so on

# Create tracks_st's df

tracks_st=df = pd.DataFrame({'tid': [1882, 1883, 1884, 1885,1886],
    'Name': ['Frantic','St. Anger','Some Kind Of Monster','Dirty Window','Invisible Kid'],
        'aid': [155, 155, 155, 155,155],
        'mtid': [1, 1, 1, 1,1],
        'gid': [3, 3, 3, 3,3],
        'u_price': [0.99, 0.99, 0.99, 0.99,0.99]})

# Create tracks_ride's df

tracks_ride=df = pd.DataFrame({'tid': [1874, 1875, 1876, 1877,1878],
    'Name': ['Fight Fire With Fire','Ride The Lightning','For Whom The Bell Tolls','Fade To Black','Trapped Under Ice'],
        'aid': [154, 154, 154, 154,154],
        'mtid': [1, 1, 1, 1,1],
        'gid': [3, 3, 3, 3,3],
        'u_price': [0.99, 0.99, 0.99, 0.99,0.99]})

# Create tracks_master's df

tracks_master=df = pd.DataFrame({'tid': [1853, 1854, 1855],
    'Name': ['Battery','Master Of Puppets','Disposable Heroes'],
        'aid': [152, 152, 152],
        'mtid': [1, 1, 1],
        'gid': [3, 3, 3],
        'composer': ['J.Hetfield/L.Ulrich', 'K.Hammett ', 'J.Hetfield/L.Ulrich'],
        'u_price': [0.99, 0.99, 0.99]})

# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master,tracks_ride,tracks_st],
                               sort=True)
print(tracks_from_albums)

# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master,tracks_ride,tracks_st],
                               ignore_index=True,
                               sort=True)
print(tracks_from_albums)

# Concatenate the tracks, show only columns names that are in all tables
# (use inner join)

tracks_from_albums = pd.concat([tracks_master,tracks_ride,tracks_st],
                               join="inner",
                               sort=True)
print(tracks_from_albums)

""" Concatenating with keys"""

# open inv_jul, inv_aug, and inv_sep csv files

inv_jul = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/inv_jul.csv",encoding= 'unicode_escape',delimiter=';')
inv_aug = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/inv_aug.csv",encoding= 'unicode_escape',delimiter=';')
inv_sep = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/inv_sep.csv",encoding= 'unicode_escape',delimiter=';')

# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul,inv_aug,inv_sep], 
                            keys=['7Jul','8Aug','9Sep'])

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind="bar")
plt.show()

""" Verifying integrity"""

# Leave the code commented until the real dataset is found

# # Concatenate the classic tables vertically
# classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# # Concatenate the pop tables vertically
# pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# # Merge classic_18_19 with pop_18_19
# classic_pop = classic_18_19.merge(pop_18_19,on="tid")

# # Using .isin(), filter classic_18_19 rows where tid is in classic_pop
# popular_classic = classic_18_19[classic_18_19["tid"].isin(classic_pop["tid"])]

# # Print popular chart
# print(popular_classic)


