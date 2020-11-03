#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 17:39:10 2020

@author: rahul
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# read spambase dataset 
df = pd.read_csv("spambase/spambase.data")
# print(df.columns)
# descriptive_statistics = df['0.64'].describe()
# print(descriptive_statistics)
# df.hist(df['0'],bins = 20, axis =1)
print(df['0'].describe())
df.hist(column='0.64',bins=10)


