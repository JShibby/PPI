#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Explore the data.
This exploration largely focused on numeric features like integers, 
and whether they were properly coded.  
This aided the construction of the data script.
But after recoding, etc., this script has useless cells and errors.


Created on Thu Apr 11 08:33:26 2019
@author: justin
"""
#%%  Packages
import numpy.random as nr

#%%  Data
# Mini data
nr.seed(0)
c = nr.choice(df.index, 1000)
dfa = df

#%%  Exploration
df.columns
df.age.describe()
df.dtypes

df[feature_cols].dtypes.value_counts()
 
#%%  Bools
columns = df.columns[df.dtypes == 'bool']
len(columns)

for col in columns:
    print(df.groupby(col)['poverty_probability'].mean().round(3),'\n')
    
#%%  Bool Graphs
# There are a lot of bools, and you don't want to graph them all at once.
columns = df.columns[df.dtypes == 'bool'][:10]

for col in columns:
    plt.figure()
    df.groupby(col)['poverty_probability'].mean().round(3).plot.bar()
    plt.title(col)    

#%% Floats
#Discovered that education_level and share_hh_income_provided are ints.     
columns = df.columns[df.dtypes == 'float64'][:-1]

#df.plot.scatter(x = 'avg_shock_strength_last_year', y='poverty_probability', alpha = 0.2)
#df.plot.hexbin(x = 'avg_shock_strength_last_year', y='poverty_probability', gridsize = 15)

for col in columns:
    plt.figure()
    df.plot.scatter(x = col, y='poverty_probability', alpha = 0.2)    
    corr = df[col].corr(df.poverty_probability).round(3)
    title = 'Correlation: '+str(corr)
    plt.title(title)
  