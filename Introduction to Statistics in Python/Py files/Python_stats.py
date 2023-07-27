# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 19:43:43 2023

@author: Brenda Rojas Delgado
"""

" cdf stands for Cumlative Distribution Function, whereas pmf stands for Probability mass function"
" Finally, rvs stands for a binomial discrete random variable (do more research)"

""" Measures of center"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# open food_consumption csv file

food_consumption =pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to Statistics in Python/Datasets/food_consumption.csv")
food_consumption.drop(food_consumption.columns[[0]], axis=1, inplace=True)

# Filter for Belgium
be_consumption = food_consumption[food_consumption['country']=='Belgium']

# Filter for USA
usa_consumption = food_consumption[food_consumption['country']=='USA']

# Calculate mean and median consumption in Belgium
print(be_consumption.agg(['mean','median']))

# Calculate mean and median consumption in USA
print(usa_consumption.agg([np.mean,np.median]))

# Subset for Belgium and USA only
be_and_usa = food_consumption[(food_consumption["country"]=='Belgium') | (food_consumption["country"]=='USA')]

# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby(by='country').agg(['mean','median']))

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption['co2_emission'].agg(['mean','median']))

""" Measures of spread"""

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'],[0,0.25,0.5,0.75,1]))

# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'],[0,0.20,0.4,0.6,0.8,1]))

# Calculate the eleven quantiles of co2_emission that split up the data into ten pieces (deciles).
print(np.quantile(food_consumption['co2_emission'],np.linspace(0,1,11)))

# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg(['std','var']))

# Create histogram of co2_emission for food_category 'beef'
beef=food_consumption[food_consumption['food_category']=='beef']
print(beef)
plt.hist(beef['co2_emission'])

# Show plot
plt.show()
plt.clf()

# Create histogram of co2_emission for food_category 'eggs'
plt.hist(food_consumption[food_consumption['food_category']=='eggs']['co2_emission'])

# Show plot
plt.show()

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby(by='country')['co2_emission'].agg('sum')

print(emissions_by_country)

# Compute the first and third quartiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3-q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]                    
print(outliers)

""" Measuring chances (dependent vs. independent variables, do more research)"""

# open amir_deals csv file
amir_deals =pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to Statistics in Python/Datasets/amir_deals.csv")
amir_deals.drop(amir_deals.columns[[0]], axis=1, inplace=True)

# Count the deals for each product
counts = amir_deals['product'].value_counts()

# Calculate probability of picking a deal with each product
probs = counts/amir_deals.shape[0]
print(probs)

# Set random seed
np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5,replace=False)
print(sample_without_replacement)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5,replace=True)
print(sample_with_replacement)

""" Discrete distributions"""

# Create resturant_groups dataframe

restaurant_groups=pd.DataFrame({'group_size':[2,4,6,2,2,2,3,2,4,2],
                   'group_id':["A","B","C","D","E","F","G","H","I","J"]})
columns_titles = ['group_id','group_size']
restaurant_groups=restaurant_groups.reindex(columns=columns_titles)

# Create a histogram of restaurant_groups and show plot
restaurant_groups['group_size'].hist(bins=[2, 3, 4, 5, 6])
plt.show()
plt.clf()

# Create probability distribution
#size_dist = restaurant_groups['group_size'] / len(restaurant_groups['group_size'])
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]

# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

print(size_dist)

# Calculate expected value
expected_value = sum(size_dist.group_size*size_dist.prob)
print(expected_value)

# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist['group_size']>=4]

# Sum the probabilities of groups_4_or_more
prob_4_or_more = sum(groups_4_or_more['prob'])
print(prob_4_or_more)

""" Continuous distributions"""

# Min and max wait times for back-up that happens every 30 min

min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting less than 5 mins
prob_less_than_5 = uniform.cdf(5,min_time,max_time)
print(prob_less_than_5)

# Calculate probability of waiting more than 5 mins
prob_greater_than_5 = 1-uniform.cdf(5,min_time,max_time)
print(prob_greater_than_5)

# Calculate the probability of waiting 10-20 mins
prob_between_10_and_20 = uniform.cdf(20,min_time,max_time)-uniform.cdf(10,min_time,max_time)
print(prob_between_10_and_20)

# Set random seed to 334
np.random.seed(334)

# Import uniform as un to shorten the library name (can be un, uf, unif, and so on)
from scipy.stats import uniform as un

# Generate 1000 wait times between 0 and 30 mins
wait_times = un.rvs(0, 30, size=1000)

# Create a histogram of simulated times and show plot
plt.hist(wait_times)
plt.show()
plt.clf()

""" The binomial distribution (with sequence of trials being independent (without replacement)"""

" Start with a simple coin flip"

# Import binom (A binomial discrete random variable)
from scipy.stats import binom

# run the coin flips code line with 8trials, with 1 as head and 0 as tail

print(binom.rvs(1,0.5,size=1)) # flip one coin, 1 time to get 1
print(binom.rvs(1,0.5,size=8)) # flip one coin, 8 times to get 1
print(binom.rvs(8,0.5,size=1)) # flip 8 coins, 1 time to get 1
print(binom.rvs(3,0.5,size=10)) # flip 3 coins, 1 times to get 1

# if the tail is heavier than the head, so probabilities are 0.25 head and 0.75 tail

print(binom.rvs(3,0.25,size=10)) # flip 3 coins, 1 times to get 1

# What is the probability of getting 7 heads?

#binom.pmf(num_heads,num_trials,prob_heads)
print(binom.pmf(7,10,0.5))

# What is the probability of getting 7 or fewer heads?

#binom.cdf(num_heads,num_trials,prob_heads)
print(binom.cdf(7,10,0.5))

# What is the probability of getting more than 7 heads?

#binom.cdf(num_heads,num_trials,prob_heads)
print(1-binom.cdf(7,10,0.5))

# Expected value=n*p (number_of_heads=prob*num_of_trials)
expected_val=10*0.5

" Simulate seals deals for Amir"

# Set random seed to 10
np.random.seed(10)

# Simulate a single deal with 30% of probability
print(binom.rvs(1, 0.3, size=1))

# Simulate 1 week of 3 deals
print(binom.rvs(3, 0.3, size=1))

# Simulate 52 weeks of 3 deals
deals = binom.rvs(3, 0.3, size=52)

# Print mean deals won per week
print(np.mean(deals))

" Calculating binomial probabilities"

# Probability of closing 3 out of 3 deals
prob_3 = binom.pmf(3,3,0.3)

print(prob_3)

# Probability of closing <= 1 deal out of 3 deals
prob_less_than_or_equal_1 = binom.cdf(1,3,0.3)

print(prob_less_than_or_equal_1)

prob_greater_than_1 = 1-prob_less_than_or_equal_1
print(prob_greater_than_1)

" How many sales will be won?"

# Expected number won with 30% win rate
won_30pct = 0.3 *3
print(won_30pct)

# Expected number won with 25% win rate
won_25pct = 0.25 *3
print(won_25pct)

# Expected number won with 35% win rate
won_35pct =  0.35 *3
print(won_35pct)

""" Normal (Bell) distribution"""

# Histogram of amount with 10 bins and show plot
#plt.hist(amir_deals.amount,bins=10)
#amir_deals['amount'].hist(bins=10)
amir_deals.amount.hist(bins=10)
plt.show()
plt.clf()

# Import norm from scipy 
from scipy.stats import norm

"Since each deal Amir worked on (both won and lost) was different, each was worth\
a different amount of money. These values are stored in the amount column of \
amir_deals and follow a normal distribution with a mean of 5000 dollars and a \
standard deviation of 2000 dollars. As part of his performance metrics, you want to \
calculate the probability of Amir closing a deal worth various amounts."

# Probability of deal < 7500
prob_less_7500 = norm.cdf(7500, 5000,2000)

print(prob_less_7500)

# Probability of deal > 1000
prob_over_1000 = 1-norm.cdf(1000, 5000,2000)

print(prob_over_1000)

# Probability of deal between 3000 and 7000
prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)

print(prob_3000_to_7000)

# Calculate amount that 25% of deals will be less than (percent point function or ppf)
pct_25 = norm.ppf(0.25, 5000,2000)

print(pct_25)

# Calculate new average amount
new_mean = 5000*(1+0.2)

# Calculate new standard deviation
new_sd = 2000*(1+0.3)

# Simulate 36 new sales (random variates, rvs)
new_sales = norm.rvs(new_mean, new_sd, size=36)

# Create histogram and show
plt.hist(new_sales)
plt.show()
plt.clf()

""" The central limit theorem or CLT (when sampling distribution resembles to\
    normal distribution as the number of trials increases, and only applies\
        when samples are independent and taken randomly) """
    
" Die without looping"
# die=pd.Series([1,2,3,4,5,6])
# samp_5=die.sample(5,replace=True)
# print(samp_5,np.mean(samp_5))

sample_means=[]                  # empty_list
die=pd.Series([1,2,3,4,5,6])
loop_num=range(1000)

for i in loop_num:              # range from 0 to 9 
    samp_5=die.sample(5,replace=True)
    sample_means.append(np.mean(samp_5))
print(np.mean(sample_means))
plt.bar(loop_num,sample_means)
plt.clf()
plt.hist(sample_means)
plt.show()
plt.clf()

" Proportions and the CLT (find out more how to get the distribution \
    of the samples proportion"

# sales_team=pd.Series(["Amir","Brian","Claire","Damian"])
# st_samp=sales_team.sample(1000,replace=True)
# plt.hist(st_samp)
# plt.show()

" The CLT in action "

" The central limit theorem states that a sampling distribution of a sample \
  statistic approaches the normal distribution as you take more samples, no \
  matter the original distribution being sampled from"

# Create a histogram of num_users and show
#amir_deals['num_users'].hist()
plt.hist(amir_deals.num_users)
plt.show()
plt.clf()

# Set seed to 104
np.random.seed(104)

# Sample 20 num_users with replacement from amir_deals
samp_20 = amir_deals['num_users'].sample(20,replace=True)

# Take mean of samp_20
print(np.mean(samp_20))

# Set seed to 104
np.random.seed(104)

sample_means = []
# Loop 100 times
for i in range(100):
  # Take sample of 20 num_users
  samp_20 = amir_deals['num_users'].sample(20, replace=True)
  # Calculate mean of samp_20
  samp_20_mean = np.mean(samp_20)
  # Append samp_20_mean to sample_means
  sample_means.append(samp_20_mean)
  
# Convert to Series and plot histogram
sample_means_series = pd.Series(sample_means)
sample_means_series.hist()

# Show plot
plt.show()
plt.clf()

# open all_deals csv file
all_deals =pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to Statistics in Python/Datasets/all_deals.csv")

""" The Poison distribution """

" Events happen at a certain rate, but completely at random \
  Probability of some # of events ocurring over a fixed period of time\
  Lambda is the average number of events per time interval"

from scipy.stats import poisson

# What is the probability that 5 puppets are adopted in a week five if lambda=8?

pet_5=poisson.pmf(5,8)

# What is the probability that less than 5 puppets are adopted in a week five if lambda=8?

pet_minus_5=poisson.cdf(5,8)

# What is the probability that more than 5 puppets are adopted in a week five if lambda=8?

pet_plus_5_8=1-poisson.cdf(5,8)

# What is the probability that more than 5 puppets are adopted in a week five if lambda=10?

pet_plus_5_10=1-poisson.cdf(5,10)

# Sampling from a Poisson distribution

pet_10w=poisson.rvs(8,size=10)  # To simulate 10 weeks with lambda=8

# Probability of 5 responses with an average of 4
prob_5 = poisson.pmf(5,4)

print(prob_5)

# Probability of 5 responses with an average of 5.5
prob_coworker = poisson.pmf(5,5.5)

print(prob_coworker)

# Probability of 2 or fewer responses
prob_2_or_less = poisson.cdf(2,4)

print(prob_2_or_less)

# Probability of > 10 responses
prob_over_10 = 1-poisson.cdf(10,4)

print(prob_over_10)

""" More probability distributions """

" Exponential distribution (probability of time between Poisson events)"

# Import expon from scipy.stats
from scipy.stats import expon

# Print probability response takes < 1 hour with an average 1 answer every 2.5-h
print(expon.cdf(1, scale=2.5))

# Print probability response takes > 4 hours
print(1-expon.cdf(4, scale=2.5))

# Print probability response takes 3-4 hours
print(expon.cdf(4, scale=2.5) -expon.cdf(3, scale=2.5))

" (Student's) T-Distribution (observations are likely to fall further from mean) "

#Look for an example

" Log-Normal Distribution (variable whose logarithm is normally distributed) "

#Look for an example

# Finally, try to plot all distributions in one plot, if possible

""" Correlation """

import seaborn as sns  # Plotting package built on top of matplotlib

# open amir_deals csv file
msleep =pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to Statistics in Python/Datasets/msleep.csv")
msleep.drop(msleep.columns[[0]], axis=1, inplace=True)

# Plot scatter with seaborn
sns.scatterplot(x="sleep_total",y="sleep_rem",data=msleep) 
plt.show()
plt.clf()

" Plot scatter with seaborn and adding linear trend to the scatter plot\
  Other ways to calculate correlation  are Kendall's thau and Spearman's rho"
                                   
sns.lmplot(x="sleep_total",y="sleep_rem",data=msleep,ci=None)
plt.show()
plt.clf()

# Compute Pearson product-moment correlation (X-Y-corr=Y-X-corr)

print(msleep.sleep_total.corr(msleep.sleep_rem))
print(msleep['sleep_rem'].corr(msleep['sleep_total']))

# open world_happiness csv file
world_happiness = pd.read_csv("C:/Users/LENOVO/OneDrive - Universidad Carlos III de Madrid/DataCamp courses/Introduction to Statistics in Python/Datasets/world_happiness.csv")
world_happiness.drop(world_happiness.columns[[0]], axis=1, inplace=True)

# Create a scatterplot of happiness_score vs. life_exp and show
sns.scatterplot(x="life_exp",y="happiness_score",data=world_happiness) 

# Show plot
plt.show()
plt.clf()

# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x="life_exp",y="happiness_score",data=world_happiness,ci=None) 

# Show plot
plt.show()
plt.clf()

# Correlation between life_exp and happiness_score
cor = world_happiness.life_exp.corr(world_happiness.happiness_score)

print(cor)

""" Correlation caveats """

# Plot a scatter of awake time vs. body weight

sns.scatterplot(x="bodywt",y="awake",data=msleep) 
plt.show()
plt.clf()

# Compute correlation

print(msleep['awake'].corr(msleep['bodywt']))

# Get distribution of body weight to see if log transformation applies

plt.hist(msleep['bodywt'],bins=10)
plt.show()
plt.clf()

# Get log transformation based on the highly skewed nature of the distribution and 
# add column to the dataset msleep. After that, make the scatter plot with trendline

msleep['log_bodywt']=np.log(msleep['bodywt'])

# Plot a scatter of awake time vs. logarithmic body weight
sns.lmplot(x='log_bodywt',y='awake',data=msleep,ci=None)
plt.show()
plt.clf()

# Compute new correlation (log(x))

print(msleep['awake'].corr(msleep['log_bodywt']))

" Other transformations apart from log transformation (log(x)) \
    a) Square-root transformation (sqrt(x)) \
    b) Reciprocal transformation (1/x) \
    c) Combinations of these, e.g. log(x) & log(y), sqrt(x) & 1/y \
\
    Correlation does not imply causation; that is, if x and y are correlated, \
    that does not mean necessarily that x causes y (spurious correlation) \
\
    Confounding (or bias) can lead to spurious correlation due to lurking variables "
    
# Scatterplot of gdp_per_cap and life_exp
sns.scatterplot(x='gdp_per_cap', y='life_exp', data=world_happiness)

# Show plot
plt.show()

# Correlation between gdp_per_cap and life_exp
cor = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])

print(cor) # correlation only measures linear relationship

# Scatterplot of happiness_score vs. gdp_per_cap
sns.scatterplot(x='gdp_per_cap',y='happiness_score',data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)

# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# Scatterplot of happiness_score vs. log_gdp_per_cap
sns.scatterplot(x='log_gdp_per_cap',y='happiness_score',data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)

# Add a new column named grams_sugar_per_day

new_col=pd.DataFrame({'grams_sugar_per_day'
                :[86.8,152,120,132,122,166,115,162,132,124,126,144,76.2,141,113,126,\
                 122,27.6,130,160,75.1,116,132,70.1,101,63.3,106,109,117,105,86.5,\
                 74.2,131,78.4,75.2,95,69.6,62.9,78,76,134,64.6,77.1,64.6,131,51.9,\
                 95.3,87.3,121,107,80.3,40.3,29.4,24.6,78.2,109,50.5,123,46.5,18.8,\
                 27.4,27.2,78.7,40.5,13,128,21.4,42.6,101,131,106,51.5,50,55.4,14.5,\
                 20.3,97.4,79.8,27.2,93.1,72.2,43.7,99.2,30.7,95.5,22.1,52.8,28.1,16.5,\
                 73.4,46.2,29.1,126,18.1,95.3,32.4,78,28.1,33.3,64.2,15.5,20.3,45.5,80.6,\
                 45.8,85,22.6,77.9,14.1,28,24.5,22.4,63.3,106,109,117,105,86.5,135,96,\
                 162,132,124,126,144,76.2,141,113,126,133,144,175,118,101,\
                 95.3,87.3,121,107,80.3,40.3,29.4,24.6,78.2]})

world_happiness['grams_sugar_per_day'] = new_col

# Scatterplot of grams_sugar_per_day and happiness_score
sns.scatterplot(x='grams_sugar_per_day',y='happiness_score',data=world_happiness)
plt.show()

# Correlation between grams_sugar_per_day and happiness_score
cor = world_happiness['grams_sugar_per_day'].corr(world_happiness['happiness_score'])
print(cor)

""" Design of experiments """

" Ways to control bias\
    a) Randomized controlled bias: participants are randomly assigned to treatment \
    or control group, and their assigment is based on chance\
    b) Placebo: resembles treatment, but has no effect, so participants do not know\
    which group they are assigned in\
    c) Double-blind trial: person administering the treatment/running experiment does \
    not know if the treatmet is real or a placebo, preventing bias in the anaysis of \
    results\
    d) Observational studies: participants are not randomly assigned to groups; they \
    asssign themselves according to certain characteristics. These studies cannot lead\
    to causation, but to association\
    "


    














    





