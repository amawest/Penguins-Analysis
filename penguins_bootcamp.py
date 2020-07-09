#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:47:24 2020
@author: Amanda West
# Data from Kaggle:
    https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data
# Analysis Helpers:
    Python: https://www.kaggle.com/parulpandey/penguin-dataset-the-new-iris/notebook
    Python: https://www.kaggle.com/amandawest/penguin-dataset-the-new-iris/edit
    R: https://github.com/allisonhorst/palmerpenguins
"""
#%% read in file

import pandas as pd 
df = pd.read_csv('/Users/amandaAmanda/Desktop/penguins_size.csv')
print(df.head())

#%% data wrangling

# data is already in good shape. 

#%% data exploration (easier to see in Jupyter Notebooks)

# 1: rows & observations 
print(df.shape)
# (344, 7) == 344 rows by 7 columns 
# 344 penguins with 7 of their characteristics described

# 2: number of each type of distinct population (3 types)
print(df['species'].value_counts())

# 3: broken down quantile data
print(df.describe(include='all'))

# 4: covariance / correlation matrix (latter easier to understand)
print(df.cov())
print(df.corr())

# 5: look at which values are missing
# missing = missing_values_table(df)
# missing


#%% basic graphs

# 1: scatter plot
import seaborn as sns
import matplotlib.pyplot as plt

# 2: Find an interesting connection using the correlation matrix.
print(df.corr())

# 3: Graph the correlation and make it colorful. 
sns.FacetGrid(df, hue="flipper_length_mm", size=8) \
   .map(plt.scatter, "flipper_length_mm", "body_mass_g") 
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.show()

#%%