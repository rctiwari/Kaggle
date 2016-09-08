# -*- coding: utf-8 -*-
"""
A Journey through Titanic

Created on Mon Sep  5 23:39:36 2016

@author: sominwadhwa
"""
#imports
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')

#Machine Learning Library Imports
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier

#Fetch Data
train_DF = pd.read_csv("/Users/sominwadhwa/Desktop/Kaggle/Titanic/train.csv", dtype = {"Age": np.float64}, )
test_DF = pd.read_csv("/Users/sominwadhwa/Desktop/Kaggle/Titanic/test.csv", dtype = {"Age": np.float64}, )

print (train_DF.head())  
print (test_DF.info())
print ("----------------------------")

#Dropping Unnecessary Data
train_DF = train_DF.drop(['PassengerId','Name','Ticket'], axis = 1, inplace = False)
test_DF = test_DF.drop(['Name','Ticket'], axis = 1, inplace = False)


#Checking probability of survival based on the place from where a passanger embarks
sns.factorplot(x = 'Embarked', y = 'Survived', data=train_DF, size = 3, aspect = 3)
figure, (ax1,ax2, ax3) = plt.subplots(1,3,figsize=(10,5))
sns.countplot(x = 'Embarked', data = train_DF, ax = ax1)
sns.countplot(x = 'Survived', hue = 'Embarked', data = train_DF, ax = ax2)
embark_perc = train_DF[["Embarked", "Survived"]].groupby(['Embarked'],as_index=False).mean()
sns.barplot(x='Embarked', y='Survived', data=embark_perc,ax=ax3)
embark_perc.head()
sns.countplot(x = 'Embarked', data = train_DF)
sns.countplot(x = 'Survived', hue = 'Embarked', data = train_DF)
#Introducing dummies for Embarked
embark_dummy = pd.get_dummies(train_DF['Embarked'])
train_DF = train_DF.join(embark_dummy) #May or may not choose to drop 'S' here (Due to lower chances of survival)
embark_dummy_test = pd.get_dummies(test_DF['Embarked'])
test_DF = test_DF.join(embark_dummy_test)
train_DF.drop(['Embarked'], axis = 1, inplace = True)
test_DF.drop(['Embarked'], axis = 1, inplace = True)
train_DF['C'] = train_DF['C'].astype(int)
train_DF['Q'] = train_DF['Q'].astype(int)
train_DF['S'] = train_DF['S'].astype(int)
train_DF['C'] = train_DF['C'].astype(int)
train_DF['Q'] = train_DF['Q'].astype(int)
train_DF['S'] = train_DF['S'].astype(int)
print (train_DF.head())

