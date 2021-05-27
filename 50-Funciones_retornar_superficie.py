# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:51:39 2021

@author: Pipe
"""

# función que le enviemos como parámetro el valor del lado de un cuadrado 
# y nos retorne su superficie.

def retornar_superficie(lado):
    sup=lado*lado
    return sup


# bloque principal del programa

va=int(input("Ingrese el valor del lado del cuadrado:"))
superficie=retornar_superficie(va)
print("La superficie del cuadrado es",superficie)

