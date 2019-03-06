# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 12:40:56 2019

@author: Killer1
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

regr = linear_model.LinearRegression()

datos = pd.read_csv('movies3.csv')

df = pd.DataFrame(datos)

print(df.head())

x=df['movie_facebook_likes']
y=df['imdb_score']

X=x[:,np.newaxis]

print(X)
print(regr.fit(X,y))
print(regr.coef_)
m=regr.coef_[0]
b=regr.intercept_
y_p=m*X+b #Prediccion
print('y={0}*x+{1}'.format(m,b))
print(regr.predict(X)[0:5])

print("Valor de R^2: ", r2_score(y,y_p))

plt.scatter(x,y,color="blue")
plt.plot(x,y_p, color="red")
plt.title('Regresion Lineal',fontsize=16)
plt.xlabel('Likes Facebook',fontsize=13)
plt.ylabel('Calificacion IMDB',fontsize=13)
plt.show()


