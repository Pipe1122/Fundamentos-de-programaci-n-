# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:43:58 2021

@author: Pipe
"""

x = int(input("Ingresa un entero, por favor: "))
if x < 0:
    x = 0
    print('Negativo cambiado a cero')
elif x == 0:
    print('Cero')
elif x == 1:
    print('Simple')
else:
    print('Más')