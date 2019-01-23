# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:28:06 2019

@author: Killer1
"""
import pandas as pd
import numpy as np

df = pd.read_csv('Data.csv',encoding = "ISO-8859-1")

print(df.info())
print(df.head())

nuevo = pd.DataFrame(df)
print(nuevo)

nuevo = nuevo.replace(np.nan,"0")
print('**********Impresion sin NaN***********')
print(nuevo.info())
print("\n"*5)
print('**********Estadisticas sin NaN***********')
print(nuevo.describe())
print("\n"*5)
print('**********Estadisticas solamente numeros***********')
print(nuevo.describe(include=[np.number]))
print("\n"*5)
nuevo = nuevo.replace("N/A","0")
nuevo = nuevo.replace("NR","0")
print("*********Estadisticas sin N/A O NR*********")

print(nuevo.describe())
print(list(nuevo))
print("\n"*5)
nuevo['Wsets'] = nuevo.Wsets.astype(int)
nuevo['Lsets'] = nuevo.Lsets.astype(int)
nuevo['WRank'] = nuevo.WRank.astype(int)
nuevo['LRank'] = nuevo.LRank.astype(int)
nuevo['W1'] = nuevo.W1.astype(int)
nuevo['L1'] = nuevo.L1.astype(int)
nuevo['W2'] = nuevo.W2.astype(int)
nuevo['L2'] = nuevo.L2.astype(int)
nuevo['W3'] = nuevo.W3.astype(int)
nuevo['L3'] = nuevo.L3.astype(int)
nuevo['W4'] = nuevo.W4.astype(int)
nuevo['L4'] = nuevo.L4.astype(int)
nuevo['W5'] = nuevo.W5.astype(int)
nuevo['L5'] = nuevo.L5.astype(int)
a = nuevo.describe()

print(nuevo.describe())

df.dropna(how='any',inplace=True)
print(df.head())
nuevo.to_csv('ATP4.csv', header=True, index= False)