# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 13:14:17 2019

@author: Killer1
"""

import pandas as pd

df = pd.read_csv('ATP4.csv', encoding = "ISO-8859-1")

print(df.info())

df.set_index("Location", inplace = True)


df_court = (df.loc[df['Court']== 'Outdoor',['Surface','Winner']])

print(df_court)

print("***************** Más Condiciones**************")

print(df.loc[(df['Series']=='Grand Slam')&(df['Surface']=='Clay')&
             (df['Winner']=='Federer R.')& (df['Round']=='The Final')])
#df_court.reset_index().to_csv("Court_ATP.csv", header = True,
                    #index = False)

