# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:08:42 2019

@author: Killer1
"""

import pandas as pd

df = pd.read_csv(r"C:\Users\Killer1\Desktop\Alvaro\BIG-DATA\CURSO-UDEMY\repositorio-github\python-ml-course-master\datasets\titanic\titanic_custom.csv")

print(df.info())

datos = pd.DataFrame(df)
d_f = pd.DataFrame(df)

df.to_csv("Personas Abordo del Titanic3.csv" ,
              header = True, index= False)

df.set_index('sex', inplace = True)

df1 = df.loc["male"]
df1.reset_index().to_csv('Male SelectTitanic.csv', header = True, 
              index=False)

df2 = df.loc["female"]
df2.reset_index().to_csv('Female SelectTitanic.csv', header = True, 
              index=False)
