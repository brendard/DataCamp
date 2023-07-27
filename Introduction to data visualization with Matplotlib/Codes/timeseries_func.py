# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 16:24:39 2023

@author: Brenda Rojas Delgado

This is a function to plot time series based on DataCamp tutorial
Course: Introduction to Data Visualization with Matplotlib

"""

# Import the required libreries
import pandas as pd
import matplotlib.pyplot as plt

# Load the climate_change csv file
climate_change = pd.read_csv(r"C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Introduction to data visualization with Matplotlib\Datasets\climate_change.csv", \
                             parse_dates=["date"], index_col="date")
    
# Define the function plot_timeseries

def plot_timeseries(axes,x,y,color,xlabel,ylabel):
    axes.plot(x,y,color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel,color=color)
    axes.tick_params('y',colors=color)

# Execute/call the function with the climate_change df
fig, ax=plt.subplots()
plot_timeseries(ax,climate_change.index,climate_change['co2'],'blue','Time','co2 (ppm)')

ax2=ax.twinx()
plot_timeseries(ax2,climate_change.index,climate_change['relative_temp'],\
                'red','Time','Relative temperature (Celsius)')

# Make annotation separately from the main function

ax2.annotate(">1 degree", xy=(pd.Timestamp("2015-10-06"),1),\
             xytext=(pd.Timestamp("2008-10-06"),-0.2),arrowprops={"arrowstyle":"->",\
                                                                  "color":"gray"})

# Display the plot
plt.show()