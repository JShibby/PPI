#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cleans out null data, recodes data, etc.  
Result is a dataframe, ready to explore, but not for sklearn.

SCRIPTS
  1. data
  *  explore
  2. encode
  3. model
  *  alt model scripts
  * present

Created on Thu Apr 11 08:32:40 2019
@author: justin
"""
#%%  Packages
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import time

#assert False

#%%  Data
print('Import ...')
t = time.time()

df = pd.read_csv('data/train_values.csv', index_col = 'row_id')
labels = pd.read_csv('data/train_labels.csv', index_col = 'row_id')
df = df.join(labels)
dfo = df

#%%  Empty columns
s = {}
for column in df.columns:
    s[column] = df[column].isnull().sum()

s = pd.Series(s)
null_tolerance = round(len(df)*.2)
empties = list(s[s > null_tolerance].index)
df = df.drop(columns = empties)

#%%  Emtpy rows
df.dropna(inplace = True) 

#%%  Low info features
columns = df.columns[df.dtypes != 'float64']
len(df.columns[df.dtypes != 'float64'])

drop_cols = []
for col in columns:
    s = df.groupby(col)['poverty_probability'].mean()
    if s.max() - s.min() < 0.05:
        drop_cols.append(col)

df = df.drop(columns = drop_cols)

#%%  Miscoded floats
#Exploration shows these floats to be integers.
col = 'education_level'
df[col].describe()
df[col].astype(int)

for col in ('education_level', 'share_hh_income_provided'):
    df[col] = df[col].astype(int)    

#%%  Categorical coding: Integers and miscoded
# recode all integers as categories.
columns = list(df.columns[df.dtypes == 'int64']) 
# add floats that are actually categories.

for col in columns:
    df[col] = df[col].astype(str)

(df.dtypes == 'int64').sum()

#%%
feature_cols = df.columns[:-1]
X = df[feature_cols]
y = df.poverty_probability
len(df)
