# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
datos = {'Nombre':
    ['Jose','Cristian','Gabriela','Mario'],
    'Calificaciones':['7','5.4','2.9','4.5'],
    'Deportes':['Futbol','Natacion','Basquetbol','Tenis'],
    'Materia':['Calculo','Quimica','Fisica','Ecuaciones Diferenciales']}
    
df = pd.DataFrame(datos)

print(df) 
print('\n'*2)
#Datos no validos
datos2 = {'Nombre':
    ['Jose','Cristian','Gabriela','N/A'],
    'Calificaciones':['7','5.4',np.nan,'4.5'],
    'Deportes':['Futbol','Natacion','N/A','Tenis'],
    'Materia':['Calculo','Quimica','Fisica','N/A']}
    
df2 = pd.DataFrame(datos2)
print(df2) 
print('\n'*2)
print(df2.info())
print('\n'*4)
#Estadisticas Básicas

print(df2.describe())
print('\n'*4)

nuevo = pd.DataFrame(df2)
nuevo = nuevo.replace(np.nan,'0')

print(nuevo)
print('\n'*4)

nuevo2 = pd.DataFrame(df2)
nuevo2.dropna(how='any', inplace=True)

print(nuevo2)
print('\n'*4)

#Eliminar Registros por Columnas
columna=df2[df2['Nombre']!='N/A']
print (columna)
print('\n'*4)
#Llenar con Ceros cualquier valor NAN en el df
nuevo3 = pd.DataFrame(df2)
nuevo3.fillna(0, inplace=True)
print(nuevo3)
print('\n'*4)
#Estadistica
print(nuevo3.describe())
print('\n'*4)
#Convertir a numero
nuevo3['Calificaciones']=nuevo3.Calificaciones.astype(float)
print(nuevo3.describe())
print('\n'*4)
#Estadisticas individuales
print("Promedio", nuevo3['Calificaciones'].mean())