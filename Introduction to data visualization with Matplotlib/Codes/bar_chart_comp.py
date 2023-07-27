# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 22:26:03 2023

@author: Brenda Rojas Delgado
"""

""" Bar-chart comparison """

" For more information about style sheets, visit: \
https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html\
\
Guidelines for choosing plotting style:\
    \
    a) Dark backgrounds are usually less visible\
    b) If color is important, consider using colorblind-friendly plotting options,\
    such as seaborn-colorblind or tableau-colorblind10\
    c) If you think someone is going to print your plots, use less ink (not ggplot)\
    d) Use gray-scale styles for black-and-white plots\
    d) "


" Why automate data?\
    a) Ease and speed\
    b) Flexibility\
    c) Robustness\
    d) Reproductibility"
    
" Note: Typing the command ls in the console will display a list of the files contained\
    in  the current working directory"
    
" Bar charts with set ax "

# Import needed libraries

import pandas as pd
import matplotlib.pyplot as plt

" Style formatting options "

# Call ggplot style format, so that the plots can be shared with others
#plt.style.use("ggplot")

# Otherwise, call plots with the default formats
#plt.style.use("default")

# You can also use Bayesian Method for Hackers style
#plt.style.use("bmh")

# Or Seaborn colorblind style
plt.style.use("seaborn-colorblind")

# Open medals_by_country csv file

medals_by_country_2016 = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to data visualization with Matplotlib/Datasets/medals_by_country_2016.csv",index_col=0)

# Create an empty plot

fig,ax=plt.subplots()

# Set parameters create a bar plot

ax.bar(medals_by_country_2016.index,medals_by_country_2016['Gold'],color="blue")

# Set labels, ticks and title

# Set x and y labels

ax.set_xlabel("Country")
ax.set_ylabel("Number of gold medals")

# Set x and y ticks
ax.set_xticklabels(medals_by_country_2016.index,rotation=90)
ax.set_yticklabels(medals_by_country_2016['Gold'],rotation=0)

# Display the figures
plt.show()
plt.clf()

" Bar charts with get ax settings "

# Create an empty plot

fig,ax=plt.subplots()

# Set parameters create a bar plot

ax.bar(medals_by_country_2016.index,medals_by_country_2016['Silver'],color="red")

# Set labels, ticks and title

# Set x and y labels

ax.set_xlabel("Country")
ax.set_ylabel("Number of gold medals")

# Set x and y ticks with get_xticks

labelx = ax.get_xticklabels()
labely = ax.get_yticklabels()
plt.setp(labelx, rotation=45, horizontalalignment='right')
plt.setp(labely, rotation=45, horizontalalignment='right')

# Display the figures
plt.show()
plt.clf()

" Visualizing bar plots together "

# Create an empty plot

fig,ax=plt.subplots()

# Set the three bar plots together (Gold, Silver, Bronze)
ax.bar(medals_by_country_2016.index,medals_by_country_2016['Gold'],\
       color="gold",alpha=0.7,label="Gold")
ax.bar(medals_by_country_2016.index,medals_by_country_2016['Silver'],\
       color="silver",alpha=0.7,bottom=medals_by_country_2016['Gold'],\
           label="Silver")
ax.bar(medals_by_country_2016.index,medals_by_country_2016['Bronze'],\
            color="darkorange",alpha=0.7,label="Bronze",\
                bottom=medals_by_country_2016['Gold']+medals_by_country_2016['Silver'])
    
## Set axes and ticks

# Set x and y labels and title

ax.set_xlabel("Country")
ax.set_ylabel("Number of gold medals")
ax.set_title("Countries with more olympic medals")

# Set x and y ticks
ax.set_xticklabels(medals_by_country_2016.index,rotation=45)
ax.set_yticklabels(medals_by_country_2016['Gold'],rotation=0)

## Add legends

ax.legend()

# Display the figures
plt.show()
plt.clf()

""" Quantitative comparison: histograms """

# Before plotting the histogram, let's plot a bar again

# Open summer2016 csv file
summer2016 = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to data visualization with Matplotlib/Datasets/summer2016.csv",index_col=0)

# Extract data from Men's Rowing and Gymnastics
mens_rowing=summer2016.loc[(summer2016['Sex'] == "M")&(summer2016['Sport'] == "Rowing")]
mens_gym=summer2016.loc[(summer2016['Sex'] == "M")&(summer2016['Sport'] == "Gymnastics")]

# Create an empty plot
fig,ax=plt.subplots()

# Get heights' mean value inside the new bar plot, adding error bars to bar charts
# yerr keyword takes an additional number and plot it as a vertical marker 

ax.bar("Rowing",mens_rowing["Height"].mean(),yerr=mens_rowing["Height"].std())
ax.bar("Gymnastics",mens_gym["Height"].mean(),yerr=mens_gym["Height"].std())
ax.set_ylabel("Height (cm)")

# Display the figures
plt.show()
plt.clf()

# Now turn these datasets into a histogram

# Create an empty plot
fig,ax=plt.subplots()

# Set bin boundaries
bin_bound=[150,160,170,180,190,200,210]

# Get heights' mean value inside the new bar plot
ax.hist(mens_rowing["Height"],label="Rowing",bins=bin_bound,histtype="step")
ax.hist(mens_gym["Height"],label="Gymnastics",bins=bin_bound,histtype="step")

# Set axes and legend
ax.set_xlabel("Height (cm)")
ax.set_ylabel("Number of observations")
ax.legend()

# Display the figures
plt.show()
plt.clf()

" Statistical plots - adding errors bars to plots "

# Open again seattle_weather and austin_weather but as pickles

seattle_weather = pd.read_pickle("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to data visualization with Matplotlib/Datasets/seattle_weather.pkl")
austin_weather = pd.read_pickle("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to data visualization with Matplotlib/Datasets/austin_weather.pkl")

# Create an empty plot
fig,ax=plt.subplots()

# Plot error bars on line plots 
# (This plot sequence in particular it works either with or without yerr keyword)
ax.errorbar(seattle_weather.loc[0:11,"MONTH"],seattle_weather.loc[0:11,"MLY-TAVG-NORMAL"],\
            yerr=seattle_weather.loc[0:11,"MLY-TAVG-STDDEV"])
ax.errorbar(austin_weather["MONTH"],austin_weather["MLY-TAVG-NORMAL"],\
            yerr=austin_weather["MLY-TAVG-STDDEV"])

# Set x and y label
ax.set_xlabel("Time (months)")
ax.set_ylabel("Temperature (Fahrenheit)")
    
# Display the figures
plt.show()
plt.clf()

" Statistical plots - adding boxplots "

# Create an empty plot
fig,ax=plt.subplots()

# Create boxplots
ax.boxplot([mens_rowing["Height"],mens_gym["Height"]])

# Set ticks and labels
ax.set_xticklabels(["Rowing","Gymnastics"])
ax.set_ylabel("Height (cm)")

# Set the size of the figure
fig.set_size_inches([5,3]) # 5-inch width, 3-inch height
    
# Display the figures
plt.show()
plt.clf()

" Quantitative comparisons: scatter plots "

# Open again climate_change as pickle

climate_change = pd.read_pickle("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to data visualization with Matplotlib/Datasets/climate_change.pkl")

# Create an empty plot
fig,ax=plt.subplots()

# Create scatter plot with a third variable encoded by color

ax.scatter(climate_change["co2"],climate_change["relative_temp"],c=climate_change.index)
 
# Set ticks and labels
ax.set_xlabel("CO2 (ppm)")
ax.set_ylabel("Relative temperature (Celsius)")
     
# Display the figures
plt.show()
plt.clf()

## Customizing scatter plots with two datasets split on decades

eighties=climate_change["1980-01-01":"1989-12-31"]
nineties=climate_change["1990-01-01":"1999-12-31"]

# Create an empty plot
fig,ax=plt.subplots()

# Create scatter plots 
ax.scatter(eighties['co2'],eighties["relative_temp"],label="eighties",color="b")
ax.scatter(nineties['co2'],nineties["relative_temp"],label="nineties",color="r")

# Add legend
ax.legend()

# Set ticks and labels
ax.set_xlabel("CO2 (ppm)")
ax.set_ylabel("Relative temperature (Celsius)")
     
# Display the figures
plt.show()
plt.clf()

## Save the files in different formats

# Save figure as png in their own folder
fig.savefig("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to data visualization with Matplotlib/Plots/CO2_temp_scatter.png",dpi=300)

# Now save figure as jpg in their own folder (take less diskspace and less bandwidth)
fig.savefig("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to data visualization with Matplotlib/Plots/CO2_temp_scatter2.jpg",pil_kwargs={"quality": 50})

# Now save figure as svg format so you can edit it after produced (Adobe Illustrator)
fig.savefig("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to data visualization with Matplotlib/Plots/CO2_temp_scatter3.svg")

" Automating figures from data "

# Getting unique values from a column

sports=summer2016["Sport"].unique()

# Create a bar chart of heights for all sports

# Create an empty plot
fig,ax=plt.subplots()

# Create a for loop to get the desired data

for sport in sports:
    sport_df=summer2016[summer2016["Sport"]==sport]
    ax.bar(sport,sport_df["Height"].mean(),yerr=sport_df["Height"].std())

# Set x ticklabel
ax.set_xticklabels(sports,rotation=90)

# Set y-label
ax.set_ylabel("Height (cm)")

# Display the figures
plt.show()
plt.clf()


