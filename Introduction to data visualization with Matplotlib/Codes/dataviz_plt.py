# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 17:20:07 2023

@author: Brenda Rojas Delgado
Course: Introduction to data visualization with Matplotlib
"""

" Import all the necessary libraries "

# Import Matplotlib module and its submodule pyplot as plt
import matplotlib.pyplot as plt  

# Import the module pandas as pd
import pandas as pd

# Import calendar to convert month integers to month names
import calendar

# importing the module display
#from IPython.display import display

" Create a dataframe of Seattle weather "

# Open seattle_weather as csv

seattle_weather = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to data visualization with Matplotlib/Datasets/seattle_weather.csv")

# Create an additional column named MONTH from DATE
seattle_weather['MONTH'] = seattle_weather['DATE']

# Apply month conversion with calendar module
seattle_weather['MONTH'] = seattle_weather['MONTH'].apply(lambda x: calendar.month_abbr[x])

# Save seattle_weather as pickle for later use

seattle_weather.to_pickle("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to data visualization with Matplotlib/Datasets/seattle_weather.pkl")

" Create a dataframe of Austin weather "

# Open austin_weather as csv

austin_weather = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to data visualization with Matplotlib/Datasets/austin_weather.csv")

# Create an additional column named MONTH from DATE
austin_weather['MONTH'] = austin_weather['DATE']

# Apply month conversion with calendar module
austin_weather['MONTH'] = austin_weather['MONTH'].apply(lambda x: calendar.month_abbr[x])

# Save austin_weather as pickle for later use

austin_weather.to_pickle("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to data visualization with Matplotlib/Datasets/austin_weather.pkl")

" Plot both dataframes "

# Create an empty plot with default axes
fig,ax=plt.subplots()

# Now it is the time to set data to axes (MONTH as x-axis and MLY-TAVG-NORMAL as y-axis)

# ax.plot(seattle_weather.loc[0:11,'MONTH'],seattle_weather.loc[0:11,'MLY-TAVG-NORMAL'])
# ax.plot(austin_weather.loc[0:11,'MONTH'],austin_weather.loc[0:11,'MLY-TAVG-NORMAL'])

# Now it is time to customize the plots
ax.plot(seattle_weather.loc[0:11,'MONTH'], seattle_weather.loc[0:11,'MLY-PRCP-NORMAL'],marker="v",linestyle="None", color="b")
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"],marker="o",linestyle="None", color="r")

# Add percentiles to Seattle weather with dotted lines and no markers
ax.plot(seattle_weather.loc[0:11,'MONTH'], seattle_weather.loc[0:11,"MLY-PRCP-25PCTL"],marker="None",linestyle="--", color="b")
ax.plot(seattle_weather.loc[0:11,'MONTH'], seattle_weather.loc[0:11,"MLY-PRCP-75PCTL"],marker="None",linestyle="--", color="b")

# Add percentiles to Seattle weather with dotted lines and no markers
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"],marker="None",linestyle="--", color="r")
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"],marker="None",linestyle="--", color="r")

# Set axes and title
ax.set_xlabel("Time (months)")
ax.set_ylabel("Average temperature (Fahrenheit degrees)")
ax.set_title("Weather patterns in Austin and Seattle")

# Display the figure
plt.show()
plt.clf()

" Repeat the procedure to use Small Multiples "

" Option 1: Three rows, two columns "

# Create an empty plot with default axes (3 rows, 2 columns)
fig,ax=plt.subplots(3,2)

# Start creating the subplots for Seattle weather separately

ax[0,0].plot(seattle_weather.loc[0:11,'MONTH'], seattle_weather.loc[0:11,'MLY-PRCP-NORMAL'],\
             color="b",marker="v")
ax[1,0].plot(seattle_weather.loc[0:11,'MONTH'], seattle_weather.loc[0:11,'MLY-PRCP-25PCTL'],\
              color="b",linestyle="--")
ax[2,0].plot(seattle_weather.loc[0:11,'MONTH'], seattle_weather.loc[0:11,'MLY-PRCP-75PCTL'],\
              color="b",linestyle="--")
    
# Start creating the subplots for Austin weather separately

ax[0,1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'],\
             color="r",marker="o")
ax[1,1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-25PCTL'],\
              color="r",linestyle="--")
ax[2,1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-75PCTL'],\
              color="r",linestyle="--")

# Display the figure
plt.show()
plt.clf()

" Option 2: Two rows, one column "

# Create an empty plot with default axes (2 rows, 1 columns)
fig,ax=plt.subplots(2,1,sharey=True)

# Start creating the subplots for Seattle weather separately

ax[0].plot(seattle_weather.loc[0:11,'MONTH'], seattle_weather.loc[0:11,'MLY-PRCP-NORMAL'],\
            marker="v",linestyle="-", color="b")

ax[0].plot(seattle_weather.loc[0:11,'MONTH'], seattle_weather.loc[0:11,'MLY-PRCP-25PCTL'],\
            marker="None",linestyle="--", color="b")

ax[0].plot(seattle_weather.loc[0:11,'MONTH'], seattle_weather.loc[0:11,'MLY-PRCP-75PCTL'],\
            marker="None",linestyle="--", color="b")
ax[0].set_ylabel("Precipitation in Seattle")
ax[0].set_title("Weather patterns in Austin and Seattle")

# Start creating the subplots for Austin weather separately

ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"],\
           marker="o",linestyle="-", color="r")
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"],\
        marker="None",linestyle="--", color="r")
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"],\
        marker="None",linestyle="--", color="r")
ax[1].set_ylabel("Precipitation in Austin")
ax[1].set_xlabel("Time (months)")

# Display the figure
plt.show()
plt.clf()

" Option 3: Two rows, two columns "

# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather.loc[0:11,"MONTH"], seattle_weather.loc[0:11,"MLY-PRCP-NORMAL"])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather.loc[0:11,"MONTH"], seattle_weather.loc[0:11,"MLY-TAVG-NORMAL"])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1,0].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1,1].plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

" Plotting time-series data with CO2 emmissions "

# open climate_change csv file. Parse object df to datetime format

climate_change = pd.read_csv(r"C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Introduction to data visualization with Matplotlib\Datasets\climate_change.csv", \
                             parse_dates=["date"], index_col="date")
    
# Save climate_change as pickle for later use

climate_change.to_pickle("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to data visualization with Matplotlib/Datasets/climate_change.pkl")

# Create an empty plot 
fig, ax = plt.subplots()

# Start loading data
ax.plot(climate_change.index,climate_change['co2'],color="b")

# Set axes
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')
plt.show()

" Plotting time-series data with relative temperatures "

# Create an empty plot 
fig, ax = plt.subplots()

# Start loading data
ax.plot(climate_change.index,climate_change['relative_temp'],color="orange")

# Set axes
ax.set_xlabel('Time')
ax.set_ylabel('Relative temperature (Celsius)')
plt.show()

" Zooming in on a decade (sixties) "

sixties=climate_change["1960-01-01":"1969-12-31"]

# Create an empty plot 
fig, ax = plt.subplots()

# Start loading data
ax.plot(sixties.index,sixties['co2'])

# Set axes
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')
plt.show()

" Zooming in on a decade (seventies) "

seventies = climate_change["1970-01-01":"1979-12-31"]

# Create an empty plot 
fig, ax = plt.subplots()

# Start loading data
ax.plot(seventies.index,seventies['relative_temp'],color='k')

# Set axes
ax.set_xlabel('Time')
ax.set_ylabel('Relative temperature (Celsius)')
plt.show()

" Zooming in on a year "

sixty_nine=climate_change["1969-01-01":"1969-12-31"]

# Create an empty plot 
fig, ax = plt.subplots()

# Start loading data
ax.plot(sixty_nine.index,sixty_nine['co2'])

# Set axes
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')
plt.show()

" Plotting two time-series together "

# Create an empty plot 
fig, ax = plt.subplots()

# Subplot C02 emmissions 
ax.plot(climate_change.index,climate_change['co2'],color="b")
# Subplot relative temperature
ax.plot(climate_change.index,climate_change['relative_temp'],color='orange')
# Set axes
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm/Relative temperature (Celsius)')
plt.show()

" Plotting two time-series together using twin axes "

# Create an empty plot 
fig, ax = plt.subplots()

# Start loading data
ax.plot(sixties.index,sixties['co2'])
ax.set_xlabel('Time',color="k")
ax.set_ylabel('CO2 (ppm)',color="blue")
# Color the first y-tick
ax.tick_params('y',colors="blue")
ax.tick_params(axis='x',colors="k")  #optional (and it only applies to the first x-axis)

# Set axes, with twin y-axes (the two plots have the same x-axes but different y-axes)

ax2=ax.twinx()
ax2.plot(sixties.index,sixties['relative_temp'],color="darkorange")
ax2.set_ylabel('Relative temperature (Celsius)',color="darkorange")
# Color the second y-tick
ax2.tick_params('y',colors="orange")

# Display the plot
plt.show()




