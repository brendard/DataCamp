# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 21:33:37 2023

@author: Brenda Rojas Delgado
"""

""" Merge method allows to join tables of different dimensions based on a common column id"""

import pandas as pd

# Open movies, taglines and financials .p file
movies = pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\movies.p')
taglines = pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\taglines.p')
financials = pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\financials.p')

# Merge movies with taglines on id (default how is 'inner')
movies_taglines=movies.merge(taglines,on="id")

# Merge movies with taglines on id using left join and compare
movies_taglines_left=movies.merge(taglines,on="id",how="left")

print(movies_taglines_left.shape)

# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isna(). sum()

# Print the number of movies missing financials
print(number_of_missing_fin)

# open csv file containing toy_store dataset
toy_story=pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/toy_story.csv",delimiter=";")
toy_story.drop(toy_story.columns[0],axis=1,inplace=True)
print(toy_story.dtypes)

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines,on="id",how="left")

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines,on="id",how="inner")

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)
