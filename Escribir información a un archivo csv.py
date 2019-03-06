# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 12:35:28 2019

@author: Killer1
"""

dic = {'Sexta Region': 'Rancagua', 'Septima Region': 'Talca', 
       'Cuarta Region': 'La Serena'}

archivo='RegionesChile.csv'

csv=open(archivo,'w')

titulo='estado,capital\n'

csv.write(titulo)

for key in dic.keys():
    estado=key
    capital=dic[key]
    filas=estado+","+capital+"\n"
    csv.write(filas)