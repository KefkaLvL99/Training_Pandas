# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:26:47 2019

@author: Killer1
"""

import pandas as pd
import numpy as np

df = pd.read_csv('Data.csv',encoding = "ISO-8859-1")

print(df.info())
print(df.head(10))
print(df.iloc[0:5]) #Permite obtener filas(reglones) de un DataFrame 
#Reglones Salteados
print(df.iloc[[0,3,6,24],]) #Llama a la fila correspondiente 0,3,6,24
#Columnas
print(df.iloc[:,0:2]) #todas las filas pero solamente columna 0 y 1
print(df.iloc[[0,3,6,24],[0,5,6]]) #reglones y luego columnas

#Rangos de reglones y columnas
print(df.iloc[0:5,5:8])