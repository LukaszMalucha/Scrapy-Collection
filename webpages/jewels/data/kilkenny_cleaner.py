# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 19:43:34 2019

@author: LukaszMalucha
"""

import pandas as pd

dataset = pd.read_csv('kilkenny.csv')


# COLUMN TYPES
dataset.dtypes

# REMOVE DUPLICATES
dataset = dataset.drop_duplicates()






################## NAMES

# remove spaces
dataset['name'] = dataset['name'].str.strip()








################# PRICE EURO

# remove coma
dataset['price_euro'] = dataset['price_euro'].str.replace(',','')

# to numeric
dataset['price_euro'] = pd.to_numeric(dataset['price_euro'])




################ DESCRIPTION
dataset['descr_1'] = dataset['descr_1'].str.strip()
dataset['descr_2'] = dataset['descr_2'].str.strip()
dataset['descr_3'] = dataset['descr_3'].str.strip()


dataset['description'] = dataset['descr_1'].map(str) + dataset['descr_2'].map(str) + dataset['descr_3'].map(str)
dataset['description'] = dataset['description'].str.replace('.,','.')




################ IMAGE_URLS





############ REMOVE OBSOLETE COLUMNS
dataset = dataset.iloc[:, [0,1,2,7,6]]


dataset.to_json('dataset_cleaned.json', orient='table', index=False)
dataset.to_csv('dataset_cleaned.csv' , encoding="utf-8", index=False) 






















