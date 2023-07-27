# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 14:30:22 2023

@author: Brenda Rojas Delgado
"""

""" Merge ordered"""

import pandas as pd
import matplotlib.pyplot as plt

# open gdp and sp500 csv files

sp500 = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/S&P500.csv")
gdp = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/gdp.csv",delimiter=";")

# Set the first column as index
gdp=gdp.set_index(gdp.iloc[:,0])
gdp.index.names = sp500.index.names
gdp.drop(gdp.columns[[0]], axis=1, inplace=True)

# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on="year", right_on="Date", 
                             how="left")

# Print gdp_sp500
print(gdp_sp500)

# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on="year", right_on="Date", 
                             how="left",fill_method='ffill')

# Print gdp_sp500
print (gdp_sp500)

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp','Returns']]

# Print gdp_returns correlation
print (gdp_returns.corr())

# Create unemployment dataframe and open inflation csv

unemployment=df = pd.DataFrame([['01/06/2013',7.5], ['01/01/2014',6.7], ['01/06/2014',6.1], 
                                ['01/01/2015',5.6],['01/06/2015',5.3],['01/01/2016',5],
                                ['01/06/2016',4.9],['01/01/2017',4.7],['01/06/2017',4.3],
                                ['01/01/2018',4.1],['01/06/2018',4],['01/01/2019',3.9],
                                ['01/06/2019',3.7],['01/01/2020',3.5]],
                               columns=['date','unemployment_rate'])

inflation = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/inflation.csv",delimiter=";")

# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation,unemployment,how="inner")

# Print inflation_unemploy 
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(x='unemployment_rate',y='cpi',kind="scatter")
plt.show()

# open gdp2 csv file

gdp2 = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/gdp2.csv",delimiter=";")

# create pop dataframe

pop= pd.DataFrame([['01/01/1990','Australia',17065100,'SP.POP.TOTL'], 
                       ['01/01/1991','Australia',17284000,'SP.POP.TOTL'],
                       ['01/01/1992','Australia',17495000,'SP.POP.TOTL'],
                       ['01/01/1993','Australia',17667000,'SP.POP.TOTL'],
                       ['01/01/1990','Sweden',8558835,'SP.POP.TOTL'],
                       ['01/01/1991','Sweden',8617375,'SP.POP.TOTL'],
                       ['01/01/1992','Sweden',8668067,'SP.POP.TOTL'],
                       ['01/01/1993','Sweden',8718561,'SP.POP.TOTL']],
                               columns=['date','country','pop','series_code'])

# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp2,pop,on=['date','country'],fill_method='ffill')

# Print ctry_date
print(ctry_date)

# Merge gdp and pop on country and date with fill (reverse the last step)
date_ctry = pd.merge_ordered(gdp2,pop,on=['country','date'],fill_method='ffill')

# Print date_ctry
print(date_ctry)

""" Merge asof"""

# open jpm, wells and bac csv files

jpm = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/jpm.csv",delimiter=";")
wells = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/wells.csv",delimiter=";")
bac = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/bac.csv",delimiter=";")

# Convert data types to an adequate format for merge_asof()

jpm["date_time"] = pd.to_datetime(jpm["date_time"])
wells["date_time"] = pd.to_datetime(wells["date_time"])
bac["date_time"] = pd.to_datetime(bac["date_time"])

# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm,wells,on="date_time",suffixes=('', '_wells'),direction='nearest')

# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells,bac,on="date_time",suffixes=('_jpm', '_bac'),direction='nearest')


# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm', 'close_wells', 'close_bac'])
plt.show()

# open gdp3 and recession csv files

gdp3 = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/gdp3.csv")
recession = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/recession.csv")

# Convert data types to an adequate format for merge_asof()

gdp3["date"] = pd.to_datetime(gdp3["date"])
recession["date"] = pd.to_datetime(recession["date"])

# Merge gdp3 and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp3,recession,on="date")
print(gdp_recession)

# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind="bar", y='gdp', x='date', color=is_recession, rot=90)
plt.show()

# open gdp4 csv file

gdp4 = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/gdp4.csv")

# Convert data types to an adequate format for merge_asof()

gdp4["date"] = pd.to_datetime(gdp4["date"])
pop["date"] = pd.to_datetime(pop["date"])

# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp4, pop, on=['country','date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# Select dates equal to or greater than 1991-01-01
recent_gdp_pop = gdp_pivot.query('date>="1991-01-01"')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()

""" Using melt to unpivot tables!"""

# open ur_wide csv file

ur_wide = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/ur_wide.csv")

# unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars=['year'], var_name='month', value_name='unempl_rate')

#Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['year'].apply(str) + '-' + ur_tall['month'].apply(str))

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values(by='date')

# Plot the unempl_rate by date
ur_sorted.plot(x='date', y='unempl_rate')
plt.show()

# open ten_yr and dji csv files

dji = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/dji.csv")
ten_yr = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/ten_yr.csv")

# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars=['metric'], var_name='date', value_name='close')

# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric=="close"')

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji, bond_perc_close, on='date', how='inner', suffixes=['_dow', '_bond'])

# Plot only the close_dow and close_bond columns
dow_bond.plot(y=['close_dow', 'close_bond'], x='date', rot=90)
plt.show()