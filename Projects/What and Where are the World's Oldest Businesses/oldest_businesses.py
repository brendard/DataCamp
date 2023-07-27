# -*- coding: utf-8 -*-
"""
Project: What and Where are the World's Oldest Businesses

Created on Thu Jul 13 15:12:59 2023

@author: Brenda Rojas Delgado
"""

"Second project from the DataCamp course"

# 1. The oldest businesses in the world

# Import the pandas library under its usual alias 
import pandas as pd

# Import display
from IPython.display import display

# Load the business.csv file as a DataFrame called businesses
businesses = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Projects/What and Where are the World's Oldest Businesses/Datasets/businesses.csv")

# Sort businesses from oldest businesses to youngest
sorted_businesses = businesses.sort_values(by='year_founded',ascending=True)

# Display the first few lines of sorted_businesses
sorted_businesses.head()

# 2. The oldest businesses in North America

# Load countries.csv to a DataFrame
countries = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Projects/What and Where are the World's Oldest Businesses/Datasets/countries.csv")

# Merge sorted_businesses with countries
businesses_countries = sorted_businesses.merge(countries,on='country_code')

# Filter businesses_countries to include countries in North America only
north_america = businesses_countries[businesses_countries['continent']=='North America']
north_america.head()

# 3. The oldest business on each continent

# Create continent, which lists only the continent and oldest year_founded
continent = businesses_countries.groupby('continent').agg({'year_founded':'min'})
print(type(businesses_countries))
                                
# Merge continent with businesses_countries
merged_continent = continent.merge(businesses_countries,on='year_founded')

# Subset continent so that only the four columns of interest are included
subset_merged_continent = merged_continent[['continent','country','business','year_founded']]
subset_merged_continent.head()

# 4. Unknown oldest businesses

# Use .merge() to create a DataFrame, all_countries
all_countries = businesses.merge(countries, on='country_code', how='right', indicator=True)

# Filter to include only countries without oldest businesses
missing_countries = all_countries[all_countries['_merge'] != 'both']

# Create a series of the country names with missing oldest business data
missing_countries_series = missing_countries['country']

# Display the series
missing_countries_series

# 4. Unknown oldest businesses (alternative method)

# # Use .merge() to create a DataFrame, all_countries
# all_countries = countries.merge(businesses,on='country_code',how='left', indicator=True)

# # Filter to include only countries without oldest businesses
# #missing_countries = all_countries[all_countries['_merge'] != 'both']
# missing_countries = all_countries[all_countries['year_founded'].isnull()]
# #missing_countries = all_countries[all_countries['year_founded'].isna()]

# # Create a series of the country names with missing oldest business data
# missing_countries_series = missing_countries['country']

# # Display the series
# missing_countries_series.head()

# 5. Adding new oldest business data

new_businesses = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Projects/What and Where are the World's Oldest Businesses/Datasets/new_businesses.csv")

# Add the data in new_businesses to the existing businesses
#all_businesses = pd.concat([businesses,new_businesses],ignore_index=True)
all_businesses = pd.concat([new_businesses,businesses], join="inner",ignore_index=True)

# Merge and filter to find countries with missing business data
new_all_countries = pd.merge(all_businesses,countries,on='country_code',how='outer',indicator=True)
new_missing_countries = new_all_countries[new_all_countries['_merge'] == 'right_only']

# Group by continent and create a "count_missing" column
count_missing = new_missing_countries.groupby(by="continent")[['country']].count()
count_missing.columns = ['count_missing']
count_missing

# 6. The oldest industries

# Import categories.csv and merge to businesses
categories = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Projects/What and Where are the World's Oldest Businesses/Datasets//categories.csv")
businesses_categories = businesses.merge(categories,on='category_code')

# Create a DataFrame which lists the number of oldest businesses in each category
count_business_cats = pd.DataFrame(businesses_categories.groupby(['category'])['business'].count())
#count_business_cats = businesses_categories.groupby('category')[['business']].agg('count')

# Create a DataFrame which lists the cumulative years businesses from each category have been operating
years_business_cats = pd.DataFrame(businesses_categories.groupby("category")['year_founded'].agg('sum'))

# Rename columns and display the first five rows of both DataFrames
count_business_cats.columns = ['count']
years_business_cats.columns = ['total_years_in_business']
display(count_business_cats.head(), years_business_cats.head())

# 7. Restaurant representation

# Filter using .query() for CAT4 businesses founded before 1800; sort results
old_restaurants = businesses_categories.query("year_founded<1800 and category_code=='CAT4'")

# Sort the DataFrame
old_restaurants = old_restaurants.sort_values(by='year_founded',ascending=True)
old_restaurants

# 8. Categories and continents

# Merge all businesses, countries, and categories together
businesses_categories_countries = pd.merge(businesses_countries,categories,on='category_code')
#businesses_categories_countries = businesses_categories.merge(countries, on='country_code')

# Sort businesses_categories_countries from oldest to most recent
businesses_categories_countries = businesses_categories_countries.sort_values(by='year_founded',ascending=True)

# Create the oldest by continent and category DataFrame
oldest_by_continent_category = businesses_categories_countries.groupby(['continent', 'category']).agg({'year_founded' : 'min'})
oldest_by_continent_category.head()