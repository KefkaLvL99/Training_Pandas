# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:54:15 2019

@author: Killer1
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

datos = pd.read_csv("student.csv")
"""
print(datos.dtypes)
print(datos.info())
print(datos.describe())
print(datos.head())
"""
df1=datos.loc[(datos['school']=='GP')] #obtener dataframe de GP
print(df1.info())

df2=datos.loc[(datos['school']=='MS')] #obtener dataframe de MS
print(df2.info())
"""
print('¿Cuantos estudiantes viajan mas de 1 hora?')
print(df1.where(df1.traveltime==4).traveltime.count())
print("Estadisticas basicas")
print(df1['traveltime'].mean())

plt.figure
df1['traveltime'].hist()
"""
"""
print('¿Cuantos estudiantes no tienen internet en casa?')
print(df1.where(df1.internet=='no').internet.count())
"""
"""
print('¿Cuantos estudiantes requieren apoyo de un tutor?')
print(df1.where(df1.famrel==1).famrel.count())

tabla = pd.pivot_table(df1, index='sex',values='famrel')
print(tabla)


print('Tabla Pivote Usuario')
agrupar=input("¿Cómo quieres agrupar los datos?")
datos1 =input("¿Cuál dato quieres analizar?") 
tablau =pd.pivot_table(df1, index=[agrupar],values=datos1,aggfunc=[np.mean,min,max])
print(tablau)
"""
#Alerta

if df1.where(df1.famrel<=2).famrel.count() > 0:
    print('Se requiere atencion especializada')
    tutores = df1.where(df1.famrel<=2).famrel.count()/2
    print('Se necesitan ', int(round(tutores)),"tutores")
