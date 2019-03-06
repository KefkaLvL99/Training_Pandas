# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:33:41 2019

@author: Killer1
"""

def pago(piezas, precio):
    costo = piezas*precio
    return(costo)


import pandas as pd

datos = pd.read_csv("precios.csv")
df = pd.DataFrame(datos)



producto = input("Introduce tu compra:\n")
piezas = int(input('¿Cuantas piezas necesitas:\n'))
precio = df[df['producto']==producto]['precio']

print(pago(piezas,precio))