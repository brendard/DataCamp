# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 21:47:09 2023

@author: LENOVO
"""

## ValueError: too many values to unpack (expected 2)

# DataFrame's labels and rows, and then use the row values to determine what color to add.

# Below is an example of how one might iterate through a music album DataFrame to print messages based upon the column genre:
# for lab, row in music_df.iterrows():
#     if row['genre'] == "Jazz":
#         print("Jazzy!")
#     elif row['genre'] == "Swing":
#         print("Slightly jazzy.")
#     else:
#         print("Not very jazzy.")

# Create the years and durations lists

years = list(range(2011,2021))
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

movie_dict = dict(zip(years, durations))

# Import pandas under its usual alias
import pandas as pd

# Create a DataFrame from the dictionary
durations_df = pd.DataFrame.from_dict(movie_dict,orient='index')

# Print the DataFrame
print(durations_df)

# Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt
fig = plt.figure()

# Draw a line plot of release_years and durations
new_plot = fig.add_subplot(111)
new_plot.plot(durations_df)

# Create a title
new_plot.set_title("Netflix Movie Durations 2011-2020")

# Show the plot
plt.show()

# Read in the CSV as a DataFrame
netflix_df=pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Intermediate Python/netflix_data/netflix_data.csv",index_col=0)

# Print the first five rows of the DataFrame
print(netflix_df.head())

# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type']=='Movie']

# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only.loc[:,['title','country','genre','release_year','duration']]

# Print the first five rows of the new DataFrame
print(netflix_movies_col_subset.head())

# Create a figure and increase the figure size
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus year
scat_plot=fig.add_subplot(111)
scat_plot.scatter(netflix_movies_col_subset.release_year,netflix_movies_col_subset.duration)

# Create a title
scat_plot.set_title("Movie Duration by Year of Release")

# Show the plot
plt.show()

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration']<=60]

# Print the first 20 rows of short_movies
print(short_movies.head(20))

# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for lab, row in netflix_movies_col_subset.iterrows() :
    if row['genre'] == "Children":
        colors.append("red")
    elif row['genre'] == "Documentaries":
        colors.append("blue")
    elif row['genre'] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")
        
# Inspect the first 10 values in your list        
colors[0:10]

# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
scat_plot=fig.add_subplot(111)
scat_plot.scatter(netflix_movies_col_subset.release_year,netflix_movies_col_subset.duration,c=colors)

# Create a title and axis labels
scat_plot.set_title("Movie Duration by Year of Release")

# Strings
xlab = 'Release year'
ylab = 'Duration (min)'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)


# Show the plot
plt.show()

# Are we certain that movies are getting shorter?
are_movies_getting_shorter = str("Hard to tell")
print(are_movies_getting_shorter)
