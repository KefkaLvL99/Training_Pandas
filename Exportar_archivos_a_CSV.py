# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 16:38:10 2019

@author: Killer1
"""

import pandas as pd

datos = pd.read_csv("Data.csv", encoding = "ISO-8859-1")

print(datos.info())

df = pd.DataFrame(datos)

df.reset_index().to_csv('Datos ExportadosATP.csv', header = True, 
              index=False)

datos.set_index("Location", inplace= True)

df1=datos.loc["Melbourne"]

df1.reset_index().to_csv('Melbourne SelectATP.csv', header = True, 
              index=False)

df2=datos.loc[datos['Series'].str.endswith("Slam")]

df2.reset_index().to_csv('Gran SlamATP.csv', header = True, 
              index=False)