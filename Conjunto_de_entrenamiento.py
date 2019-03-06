# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:51:41 2019

@author: Killer1
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

datos = pd.read_csv("moviesc10.csv")

df= pd.DataFrame(datos)

x=df['cast_total_facebook_likes']
y=df['imdb_score']

print('Datos Originales')
print(df.head(10))
X_train,X_test,Y_train,Y_test = train_test_split(x,y, test_size = 0.7, random_state=42)

print("X_train")
print(X_train)
print("Y_train")
print(Y_train)

X_train = X_train.values.reshape([X_train.values.shape[0],1])
X_test = X_test.values.reshape([X_test.values.shape[0],1])
regr = linear_model.LinearRegression()
regr.fit(X_train,Y_train)
y_pred=regr.predict(X_test)

plt.scatter(X_train,Y_train,color='blue')
plt.scatter(X_test,y_pred,color='red')

print('Error : ', mean_squared_error(Y_test,y_pred))
print('El valor de R^2:',r2_score(Y_test,y_pred ))
