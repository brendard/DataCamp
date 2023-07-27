# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:41:54 2023

@author: Brenda Rojas Delgado
"""

import pandas as pd
import matplotlib.pyplot as plt

# Open movies and genres .p file
movies = pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\movies.p')
movie_to_genres = pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\movie_to_genres.p')

m = movie_to_genres['genre'] == 'Action'
action_movies = movie_to_genres[m].head()

scifi_movies=movie_to_genres [movie_to_genres['genre'] =="Science Fiction"]

pop_movies=movies.merge(movie_to_genres, how='right',left_on='id', right_on='movie_id').groupby('genre').count().sort_values(by='popularity', ascending=False).head(10)

""" Right join"""

# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies,on="movie_id",how="right")

# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act','_sci'))

# Print the first few rows of action_scifi to see the structure
print(action_scifi.head())

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(scifi_only, how='inner',left_on='id', right_on='movie_id')
                                  
# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)

# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(pop_movies, how='right', 
                                      left_on='movie_id', 
                                      right_on='id')

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()

""" Outer join"""

# Open MCU movies .csv file
MCU = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Joining Data with Pandas/Datasets/MCU_movies_Dataset.csv",encoding= 'unicode_escape')

# Get Iron Man 1 and 2 casts' dataset

iron_1_actors=MCU[MCU['Title']=='Iron Man'].filter(like='Cast')
iron_2_actors=MCU[MCU['Title']=='Iron Man 2'].filter(like='Cast')

# Create Dataframes only with actors and appearance order

iron_1_actors=iron_1_actors["Cast"].str.split(",", expand=True).T
iron_1_actors.index.names = ['app_order']
iron_1_actors.rename(columns={ iron_1_actors.columns[0]: "actor" }, inplace = True)

iron_2_actors=iron_2_actors["Cast"].str.split(",", expand=True).T
iron_2_actors.index.names = ['app_order']
iron_2_actors.rename(columns={ iron_2_actors.columns[0]: "actor" }, inplace = True)

# Merge iron_1_actors to iron_2_actors on index with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,  how="outer", on="app_order", suffixes=('_1','_2'))                                                               

# Create an index that returns true if the same actor was in both movies and appeared the first
m = ((iron_1_and_2['actor_1']).isin(["Robert Downey Jr.","Gwyneth Paltrow"]) | 
    (iron_1_and_2['actor_2']).isin(["Robert Downey Jr.","Gwyneth Paltrow"]))

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())

""" Joins with itself"""

# Open crews .p file
crews = pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\crews.p')

# Merge the crews table to itself
crews_self_merged = crews.merge(crews,how="inner",on="id",suffixes=('_dir','_crew'))

# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner',
                                suffixes=('_dir','_crew'))

# Create a Boolean index to select the appropriate avoidance of Director in both left and right tables
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & 
    (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())

""" Merging on indexes"""

# Open ratings .p file
ratings = pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\ratings.p')

# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings,on="id")

# Print the first few rows of movies_ratings
print(movies_ratings.head())

# Open sequels and financials .p file
sequels = pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\sequels.p')
financials = pd.read_pickle(r'C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Joining Data with Pandas\Datasets\financials.p')

# Merge sequels and financials on index id,ensuring that all the rows from the sequels are returned and some rows from the other table may not be returned 
sequels_fin = sequels.merge(financials,on="id",how="left")

# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how="inner", left_on="sequel", right_on="id", suffixes=('_org','_seq'))

# Fix this code line so that right index works
#orig_seq = sequels_fin.merge(sequels_fin, how="inner", left_on="sequel", right_on="id", right_index=True, suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq 
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff 
titles_diff = orig_seq[["title_org","title_seq","diff"]]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values('diff', ascending=False).head())