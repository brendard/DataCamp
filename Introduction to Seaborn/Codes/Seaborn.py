# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 21:35:53 2023

@author: Brneda Rojas Delgado

Course: Introduction to Seaborn  by DataCamp

Disclaimer: Even though this course is entirely delivered by DataCamp,
some code lines are made by the author of this py file, as a way to show
personal progress beyond the course content.

Summary:
    
    Seaborn is a Python library for data visualization to easily create the most 
common plots. Several advantages can be offered with the use of the Seaborn library:
    
    a) Easy to use
    b) Works well with pandas data structures
    c) Built on top on Matplotlib
    d) In a DataFrame, Seaborn automatically adds the name of the column as the
    x-axis/y-axis label at the bottom (x) or to the left (y)
    e) Seaborn works great with DataFrame, only if the df is tidy
    f) Allows the access to built-in datasets
    g) Allows to add a third variable with key-word hue (with or without using pandas, 
    so variables can be either list or dataframe columns). Setting hue will create
    subgroups that are displayed as different colors on a single plot. 
    h) It allows to subgroup by row, column, hue, point size, style, and transparency
    i) Combining size and hue keywords on relplot() allows to categorize by size and color
    with the same parameter       
    j) Seaborn also supports more advanced visualizations and analyses like linear
    regressions                                
    
What else hue does?

    It is a key-word that allows to assert more control over the ordering and coloring
of each value. The "hue" order parameter takes in a list of values and will set the the
order of the values accordingly

Relational plots, whose function is known as relplot(), is a command that enables to
visualize the relationship between two quantitative variables using either line plots
or scatter plots. The biggest advantage of relplot() is that subplots can be created 
in a single figure.

There are two types of relational plots:
    
    a) Scatter plots: each plot point is an independent observation
    b) Line plots: each plot point represents the same "thing" tipically tracked over time                                                      

Examples of relational plots:
    
    a) Height vs. Weight
    b) Number of school absences vs. final grades
    c) GDP vs. percentage of literates

Note: There are some plots with overcrowded y-axes. Solutions for that problem are yet to be
found. However, a foor loop based on percentages of the values has been rehearsed. The accuracy
or mathematical validity of such approach is under study.   

Categorical plots show the distribution of a quantitative variable within categories
defined by a categorical variable.

Examples of categorical plots: bar plots, count plots, box plots, point plots

Catplot() allows to represent categorical plots, having the same advantages of relplot(),
such as creating easily subplots with rows and columns. Even though catplot and count plot 
can work the same, they have differences.            

Alternatively, you can use relplot() and catplot()'s row and/or col to create subgroups that
are displayed on separate subplots.                          

What is a boxplot?

    A boxplot is a figure that shows the distribution of quantitative data. Through these, 
median, spread, skewness, and outliers can be seen, what facilitates the comparison of
distributions among data groups.

    By default, the whiskers extend to 1.5* the interquartile range (IQR), but the whis
parameter can be used to change the whiskers. Here are some examples:
    
    a) whis=2.0 sets IQR from 1.5 to 2 times
    b) whis=[5,95] sets IQR to show the data range from 5 to 95 pctl               
    c) whis=[0,100] sets IQR to show the entire range of data  
                                                         
What are point plots?

    Point plots are graphics that show mean of quantitative variable, where vertical lines
represent the 95% of the confidence intervals. Confidence intervals show the level of uncer-
tainty about mean estimates.

    Point plots and line plots show the same information (mean of quantitative variable and 95%
confidence intervals for the mean), but there are key differences:
    
    a) Line plot has quantitative variable (usually time) on x-axis
    b) Point plot has categorical variable on x-axis
                                                         
    On the other hand, Point plots and bar plots show the same information, such as mean of 
quantitative variable and 95% confidence intervals for the mean, but there are key differences:
    
    a) Line plot has quantitative variable (usually time) on x-axis
    b) Point plot has categorical variable on x-axis
                                                         
Preset style options: "white", "dark", "whitegrid", "darkgrid","ticks", and they are all set 
with the sns.set_style() function

Preset plotting palette with some divergent palettes: red/blue ("RdBu"), purple/green ("PRGn"),
as well as their reversed versions: "RdBu_r" and "PRGn". Besides, sequential palettes can be 
also used: "Greys", "Blues", "PuRd", and "GnBu". Use sns.set_palette() function to do settings.
Finally, you can also set a custom palette, like this one:
    
    custom_palette=["red","green","orange","blue","yellow","purple"]
    sns.set_palette(custom_palette)

You can set the context with the next dic options: {paper, notebook, talk, poster}

FacetGrid vs. AxesSubplot objects

Seaborn plots create two different types of objects: FacetGrid and AxesSubplot

Object Type     Plot types                         Characteristics             Add title
FacetGrid       relplot(),catplot()                Can create subplots         g.fig.suptitle()
AxesSubplot     scatterplot(), countplot(),etc.    Only creates a single plot  g.set_title()

Notes:
    - The `ci` parameter is deprecated. Use `errorbar=None` for the same effect.
                                                         
"""

" Get started by importing all needed libraries "

# Import seaborn as sns 
import seaborn as sns 

# Import Matplotlib as plt 
import matplotlib.pyplot as plt

# Import pandas as pd
import pandas as pd

# Import numpy as np
import numpy as np

" Set plotting style "

#sns.set_style("white") # default background style
sns.set_style("darkgrid") # default background style

" Set plotting palette "

#sns.set_palette("RdBu") 

" Set plotting context "
# Change the context to "notebook"
sns.set_context("notebook")

# Create a scatter plot. But first, create height and wave lists 

height=[62,64,69,75,66,68,65,71,76,73]

weight=[120,136,148,175,137,165,154,172,200,187]

sns.scatterplot(x=height,y=weight)

# Display the figure

plt.show()
plt.clf()

# Now create a count plot, but create first a count list to represent categorical lists

gender=["Female","Female","Female","Female","Male","Male","Male","Male","Male","Male"]
sns.countplot(x=gender)

" Use seaborn to plot gps versus phones per 1k people "

# Open csv file "countries_of_the_world"

countries=pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to Seaborn/Datasets/countries-of-the-world.csv",decimal=',')

# Create scatter plot of gdp vs phones, and gdp vs percent_literate

from matplotlib.ticker import PercentFormatter

ax=sns.scatterplot(x="GDP ($ per capita)",y="Phones (per 1000)",data=countries)
ax.yaxis.set_major_formatter(PercentFormatter(100))
#plt.yticks(rotation=90)
for index, label in enumerate(ax.get_yticklabels()):
   if index % 10 == 0:
      label.set_visible(True)
   else:
      label.set_visible(False)

# Display the figure

plt.show()
plt.clf()

sns.scatterplot(x=countries["GDP ($ per capita)"],y=countries["Literacy (%)"])

# Display the figures

plt.show()
plt.clf()

# Create separate countplots with the column Region  with different methods
# (using dfs with countplot)

sns.countplot(y=countries["Region"])

# Display the figure

plt.show()
plt.clf()

sns.countplot(x="Region",data=countries)
plt.xticks(rotation=45)

# Display the figure

plt.show()
plt.clf()

" Use seaborn to get plots from a different dataset "

# Open csv file "young-people-survey-responses"

csv_filepath="C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to Seaborn/Datasets/young-people-survey-responses.csv"
ypsr = pd.read_csv(csv_filepath,index_col=0)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x="Spiders",data=ypsr)

# Display the plot
plt.show()

" Add a third variable with hue "

# Load a built-in dataset. In this case, load the tips dataset

tips=sns.load_dataset("tips")

# Create a scatter plot from tips, adding a third variable "smoker" with key-word hue

# First, specify the hue colors with html-coded color palette

hue_colors_html={"Yes":"#808080","No":"#00FF00"}

sns.scatterplot(x="total_bill",y="tip",data=tips,hue="smoker",hue_order=["Yes","No"],\
                palette=hue_colors_html)

# Display the figure

plt.show()
plt.clf()

" Use hue with countplots "

# Plot a countplot with hue on tips dataframe
hue_colors={"Female":"hotpink","Male":"dodgerblue"}
sns.countplot(x="smoker",data=tips,hue="sex",palette=hue_colors)

# Display the figure
plt.show()
plt.clf()

" Hue and scatter plots "

# Open csv "student-alcohol-consumption"
students_data="C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to Seaborn/Datasets/student-alcohol-consumption.csv"
students_df = pd.read_csv(students_data,index_col=0)

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x="absences",y="G3",data=students_df,hue="location",hue_order=["Rural","Urban"])

# Show plot
plt.show()
plt.clf()

" Use again hue with countplots "

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x="school",data=students_df,hue="location",hue_order=["Rural","Urban"],\
                palette=palette_colors)

# Display plot
plt.show()
plt.clf()

" Introduction to relational plots and subplots "

# Create a relational scatter plot from dataframe tips (use col or row keyword as separator)

sns.relplot(x="total_bill",y="tip",data=tips,kind="scatter",col="smoker",row="time")

# Display plot
plt.show()
plt.clf()

# Now, create the same scatter plot based on the days of the week
sns.relplot(x="total_bill",y="tip",data=tips,kind="scatter",col="day",size="size",
            hue="size",style="smoker",alpha=1)

# Display plot
plt.show()
plt.clf()

# Finally, create relplot based on subsetted categories (Fri and Sat, subsetting only with
# col_order)

sns.relplot(x="total_bill",y="tip",data=tips,kind="scatter",col="day",col_order=["Fri","Sat"],
            size="size")

# Display plot
plt.show()
plt.clf()

# Let's create a relplot with row from students_df

# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", data=students_df, kind="scatter",row="study_time")

# Show plot
plt.show()
plt.clf()

# Let's create a relplot with col from students_df

# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=students_df,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"])

# Show plot
plt.show()
plt.clf()

# Create a relplot with both row and column together 

# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", data=students_df,
            kind="scatter", col="schoolsup",
            row="famsup", col_order=["yes", "no"],
            row_order=["yes", "no"],alpha=0.7)

# Show plot
plt.show()

" Changing the size of scatter plot points "

# Open the csv file mpg

mpg=pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to Seaborn/Datasets/mpg.csv")

# Create scatter plot of horsepower vs. mpg using cylinders as size format
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, hue="cylinders",kind="scatter", 
            size="cylinders")

# Show plot
plt.show()

# Create a scatter plot of acceleration vs. mpg using the origin as style format
sns.relplot(x="acceleration", y="mpg", 
            data=mpg, hue="origin",kind="scatter", 
            size="cylinders",style="origin")

# Show plot
plt.show()

" Introduction to line plots with Seaborn "

# Open air_quality csv file and remove empty columns
air_qual=pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to Seaborn/Datasets/AirQualityUCI.csv",
                      delimiter=";")
air_qual=air_qual.drop(air_qual.columns[[15, 16]],axis = 1)

# Calculate mean values per hour 
mean_NO2 = air_qual[['NO2(GT)']].groupby(air_qual['Time'],as_index=False).mean()

# Get categorical values of the air_qual df

time_ind=pd.DataFrame(np.array(pd.Categorical(air_qual['Time']).categories))

mean_NO2 =mean_NO2.set_index(time_ind.iloc[:,0])

# Create a relational scatter plot
sns.relplot(x=mean_NO2.index,y="NO2(GT)",data=mean_NO2,kind="scatter")
plt.xticks(rotation=90)
plt.show(), plt.clf()

# Create a relational line plot
sns.relplot(x=mean_NO2.index,y="NO2(GT)",data=mean_NO2,kind="line",ci=None)
plt.xticks(rotation=90)
plt.show(), plt.clf()

# Create a relational scatter plot with hue, kind and style to subgroup
# (this is not the best plotting option, tho)

sns.relplot(x="Date",y="NO2(GT)",data=air_qual,kind="scatter",
            style="Time",hue="Time",hue_order=mean_NO2.index)
plt.xticks(rotation=45)
plt.show(), plt.clf() 

#A better plotting option would be getting the mean value by date, but it has to be reviewed
Mean_no2_by_date=air_qual.groupby(['Date'])["NO2(GT)"].mean().to_frame()

sns.relplot(x=Mean_no2_by_date.index,y="NO2(GT)",data=Mean_no2_by_date,
            kind="scatter")
plt.xticks(rotation=90)
plt.show(), plt.clf() 

# Still, the x-axis is too crowded. Let's plot with datetime index
air_qual_2=air_qual.copy()
air_qual_2["Datetime"] = air_qual_2["Date"].astype(str) +"-"+ air_qual_2["Time"]
air_qual_2["Datetime"]=pd.to_datetime(air_qual_2["Datetime"],format='%d/%m/%Y-%H.%M.%S')
air_qual_2=air_qual_2.drop(['Date', 'Time'],axis = 1)
air_qual_2 = air_qual_2.set_index('Datetime')

sns.relplot(x=air_qual_2.index,y=air_qual_2["NO2(GT)"],data=air_qual_2,
              kind="scatter")
plt.show(), plt.clf() 

" Interpreting line plots from mpg dataframe "

# Create line plot (relplot automatically creates the line intervals, the same
# as ci=95)
sns.relplot(x="model_year",y="mpg",data=mpg,kind="line",ci=95)
# Show plot
plt.show(), plt.clf()

# relplot is a figure-level function and does not accept the `ax` parameter. 
# You may wish to try lineplot to display lines with confidence intervals
# on separate subplots

fig, (ax1, ax2) =plt.subplots(1, 2)
sns.lineplot(ax=ax1,x="model_year", y="mpg", data=mpg, color="orange")
sns.lineplot(ax=ax2,x="model_year", y="mpg", data=mpg,errorbar="sd")

# Show plot
plt.show(), plt.clf()

# Create line plot of model year vs. horsepower with ci turned off
sns.relplot(x="model_year",y="horsepower",data=mpg,kind="line", ci=None)

# Show plot
plt.show(), plt.clf()

# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None,hue="origin",style="origin",
            markers=True, dashes=False)

# Show plot
plt.show(), plt.clf()

" Categorical plots: count plots and bar plots "

# Create a countplot and later a catplot on ypsr to compare. 
# If possible, plot them in the same figure. 
# UserWarning: catplot is a figure-level function and does not accept target axes.
# You may wish to try countplot

sns.countplot(x="Internet usage",data=ypsr).set(title='Internet usage')
plt.xticks(rotation=45)

# Show plot
plt.show(), plt.clf()

categories=pd.DataFrame(np.array(pd.Categorical(ypsr['Internet usage']).categories))
cat_order=pd.DataFrame([categories.iloc[3],categories.iloc[1],
                        categories.iloc[0],categories.iloc[2]])
sns.catplot(x="Internet usage",data=ypsr, kind="count",
            order=cat_order.iloc[:,0]).set(title='Internet usage')
plt.xticks(rotation=45)

# Show plot
plt.show(), plt.clf()

# Now create a bar plot from tips dataset setting the kind as bar (you can also set ci)
# It is a more commom practice to put categorical variables on x-axis, but you can
# change the orientation

sns.catplot(y="day",x="total_bill",data=tips, kind="bar").\
    set(title='Total bills per day')

# Show plot
plt.show(), plt.clf()

# Separate into column subplots based on gender
sns.catplot(y="Internet usage", data=ypsr,
            kind="count",col="Gender")

# Show plot
plt.show(), plt.clf()

# Separate into column subplots based on age category
ypsr['Age Category'] = np.where(ypsr['Age']<21, 'Less than 21', '21+')
sns.catplot(y="Internet usage", data=ypsr,
            kind="count",col='Age Category')

# Show plot
plt.show(), plt.clf()

## This command sequence, can be also applied to get age categories
# p = pd.DataFrame([ypsr['Age']<21])
# p=p.transpose()
# ypsr['Age Category']=p

" Bar plots with categories based on interest "

classification = {
    0: 'Unknown/Unanswered',
    1: 'Very uninterested',
    2: 'Somewhat uninterested',
    3: 'Neutral',
    4: 'Somewhat interested',
    5: 'Very interested'
}

ypsr['Interested in Math']=ypsr["Mathematics"].map(classification)

# Create a count plot of interest in math, separated by gender
sns.catplot(y="Interested in Math",data=ypsr,kind="count")

# Show plot
plt.show()

# Now create another category based on real interest in math
ypsr['Really interested?'] = np.where(ypsr['Mathematics']<=3, False, True)

# Create a bar plot of interest in math, separated by gender
sns.catplot(x="Gender",y="Really interested?",data=ypsr,kind="bar")

# Show plot
plt.show(), plt.clf()

# Create bar plot of average final grade in each study category
# List of categories from lowest to highest
# Turn off the confidence intervals

category_order = ["<2 hours", 
                  "2 to 5 hours", 
                  "5 to 10 hours", 
                  ">10 hours"]

sns.catplot(x="study_time",y="G3",data=students_df,kind="bar",
            order=category_order,ci=None)

# Show plot
plt.show(), plt.clf()

" Creating bloxplots "

# Create a boxplot from tips dataset and use Catplot
# Reverse the order of the boxplots: Dinner first, lunch second
# Use sym="" keyword to omit outliers 

g=sns.catplot(x="time",y="total_bill",data=tips,kind="box",
              order=["Dinner","Lunch"],sym="")

# Show plot
plt.show(), plt.clf()

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x="study_time",y="G3",data=students_df,order=study_time_order,kind="box")

# Show plot
plt.show(), plt.clf()

# Create a box plot with subgroups and omit the outliers
sns.catplot(x="internet",y="G3",data=students_df,kind="box",
hue="location",sym="")

# Show plot
plt.show(), plt.clf()

# Set the whiskers to 0.5 * IQR
sns.boxplot(x="romantic", y="G3", data=students_df,whis=0.5)

# Show plot
plt.show(), plt.clf()

# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3", data=students_df,kind="box", whis=[5,95])

# Show plot
plt.show(), plt.clf()

# Extend the whiskers at the min and max values
sns.boxplot(x="romantic", y="G3", data=students_df, whis=[0,100])

# Show plot
plt.show(), plt.clf()

" Creating point plots "

# Create a point plot of family relationship vs. absences
# Add caps to the confidence interval
# Remove the lines joining the points
sns.catplot(x="famrel",y="absences",data=students_df,kind="point",
            capsize=0.2, join=False)
            
# Show plot
plt.show(), plt.clf()

# Import median function from numpy
from numpy import median

# Create a point plot that uses color to create subgroups
# Turn off the confidence intervals for this plot
sns.pointplot(x="romantic",y="absences",data=students_df,hue="school",
              ci=None, estimator=median)

# Show plot
plt.show(), plt.clf()

" Edit color and style "

# Add category to Parent's advice and create a new column (use the same 
# method as with classification) 

category_order_2 ={
    1: 'Never',
    2: 'Rarely',
    3: 'Sometimes',
    4: 'Often',
    5: 'Always'
}

ypsr["Follow parents' advice?"]=ypsr["Parents' advice"].map(category_order_2)

# Create a count plot of survey responses
g=sns.catplot(x="Follow parents' advice?",data=ypsr,kind="count",
          palette="RdBu", order=["Never", "Rarely", "Sometimes", 
                  "Often", "Always"])

# Show plot
plt.show(), plt.clf()

# Create bar plot with the number of siblings on x-axis and loneliness on y-axis
sns.catplot(x="Siblings", y="Loneliness",
            data=ypsr, kind="bar")

# Show plot
plt.show(), plt.clf()

# Get number of siblings by groups with if sentence (0, between 1-3 and 3+) Find out later

col         = "Siblings"
conditions  = [ ypsr['Siblings']==0, ypsr['Siblings']<3, ypsr['Siblings']>=3 ]
choices     = [ "No siblings", 'Less than 3', '3+' ]

ypsr["Siblings' group"] = np.select(conditions, choices, default=np.nan)

ypsr["Feels lonely"]=pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to Seaborn/Datasets/feels_lonely.csv")
 
sns.catplot(x="Siblings' group", y="Feels lonely",data=ypsr,
            kind="bar",order=["No siblings","Less than 3","3+"])
# Show plot
plt.show(), plt.clf()

sns.catplot(x="Siblings' group", y="Loneliness",data=ypsr,
            kind="bar",order=["No siblings","Less than 3","3+"])

# Show plot
plt.show(), plt.clf()

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=ypsr, kind="box",
            palette=["#39A7D0","#36ADA4"])

# Show plot
plt.show(), plt.clf()

" Adding titles and labels - Part 1 (FacetGrid) "

# Adding title to FacetGrid

# Create a scatter plot from height vs weight lists

g=sns.scatterplot(x=height,y=weight)
plt.xticks(rotation=45)

# Show plot
plt.show(), plt.clf()

# Plot Region vs. Birthrate from mpg and create a Group column: Group 1 for 
# countries with less than 100MM and Group 2 for otherwise

countries['Pop group'] = np.where(countries['Population']<10000000, 
                                  'Less than 10MM', '10MM+')

h=sns.catplot(x="Region",y='Birthrate',data=countries,kind="box",
              col='Pop group',col_order=['Less than 10MM', '10MM+'])
h.fig.suptitle("Region vs. Birthrate",y=1.03)
h.set_xticklabels(rotation=90)
h.set_titles("This is {col_name} Population")
h.set(xlabel="Region of the world",ylabel="Birthrate of world population")

# Show plot
plt.show(), plt.clf()

# Identify what type of object plot g is and assign it to the variable type_of_g

# Create scatter plot
i = sns.relplot(x="weight", y="horsepower", data=mpg,kind="scatter")

# Identify plot type
type_of_i = type(i)

# Print type
print(type_of_i)

# Create scatter plot from mpg (Car Weight vs. Horsepower)
j = sns.relplot(x="weight", y="horsepower", data=mpg, kind="scatter")

# Add a title "Car Weight vs. Horsepower"
j.fig.suptitle("Car Weight vs. Horsepower",y=1.03)

# Show plot
plt.show(), plt.clf()

" Adding titles and labels - Part 2 (AxesSubplot) "

# Plot Region vs. Birthrate from mpg and compare to FacetGrid method done before

# AttributeError: 'FacetGrid' object has no attribute 'set_title'. That is why
# catplot, kind="box" cannot be used. Use boxplot() instead

k=sns.boxplot(x="Region",y='Birthrate',data=countries, hue="Pop group")
k.set_title("Region vs. Birthrate",y=1.03)
k.set_xticklabels(k.get_xticklabels(),rotation=90)
k.set(xlabel="Region of the world",ylabel="Birthrate of world population")

# Show plot
plt.show(), plt.clf()

# Get a lineplot from the mpg_mean data frame. mpg_mean is the result of getting the
# mean value of mpgs grouped by region

mpg_mean=mpg.groupby(["model_year", "origin"]).agg(mpg_mean=('mpg', 'mean')).reset_index()

# Create line plot
l = sns.lineplot(x="model_year", y="mpg_mean", data=mpg_mean, hue="origin")

# Add a title "Average MPG Over Time"
l.set_title("Average MPG Over Time")


# Add x-axis and y-axis labels
l.set(xlabel="Car Model Year", ylabel="Average MPG")


# Show plot
plt.show(), plt.clf()

# Get a pointplot with catplot() function from mpg dataset

# Create point plot
sns.catplot(x="origin", 
            y="acceleration", 
            data=mpg, 
            kind="point", 
            join=False, 
            capsize=0.1)

# Rotate x-tick labels
plt.xticks(rotation=90)

# Show plot
plt.show()

" Putting all together "

# Open survey_data csv file

survey_data=pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to Seaborn/Datasets/survey_data.csv")

# Adjust to add subgroups based on "Interested in Pets" (FacetGrid)
m = sns.catplot(x="Gender",
                y="Age", data=survey_data, 
                kind="box", hue="Interested in Pets")

# Set title to "Age of Those Interested in Pets vs. Not"
m.fig.suptitle("Age of Those Interested in Pets vs. Not")

# Show plot
plt.show()

# Adjust to add subplots per gender who likes Techno (AxesSubplot)
n = sns.barplot(x="Village - town", y="Likes Techno", 
                data=survey_data, hue="Gender")

# Add title and axis labels
n.set_title("Percentage of Young People Who Like Techno", y=1.02)
n.set(xlabel="Location of Residence", 
       ylabel="% Who Like Techno")

# Show plot
plt.show()