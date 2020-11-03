#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:49:44 2020

@author: rahul
"""
import pandas as pd
from sklearn import linear_model
from sklearn import svm

data = pd.read_csv('spambase/spambase.data')

# data is not suffled 

data = data.sample(frac=1)

# split the dataset 

X = data.drop('1',axis= 1)
Y = pd.DataFrame(data,columns=['1'])

# model creation
model = svm.SVC()
model.fit(X,Y)
accuracy = model.score(X,Y)
print(accuracy)