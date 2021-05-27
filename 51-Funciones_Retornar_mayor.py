# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:42:30 2021

@author: Pipe
"""

# Función que le enviemos como parámetros dos enteros y nos retorne el mayor.

def retornar_mayor(v1, v2):
    if v1>v2:
        mayor = v1
    else:
        mayor = v2
    return mayor

# Bloque principal
valor1 = int(input("Ingrese el primer valor:"))
valor2 = int(input("Ingrese el segundo valor:"))
print(retornar_mayor(valor1, valor2))


