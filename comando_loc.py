# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 12:53:47 2019

@author: Killer1
"""

import pandas as pd
import numpy as np

datos = pd.read_csv('Data.CSV',encoding = "ISO-8859-1")

print(datos.head())
datos.set_index("Location",inplace=True)
print("Melbourne")
print(datos.loc["Melbourne"])
print(["Atlanta y Superficie"])
print(datos.loc["Atlanta","Surface"])
print("Seleccion Amplia")
print(datos.loc[["Atlanta","Melbourne"],["Series","Court"]])
print("Seleccion Con Rango")
print(datos.loc[["Atlanta","Melbourne"],"Series":"Round"])
print("Seleccion solamente de Grand Slam")
print(datos.loc[datos['Series'].str.endswith('Slam')])