# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:35:21 2021

@author: Pipe
"""

a, b = 0, 1
# La variable a y b toman simultaneamente los valores 0 y 1. 

while b < 100:
# El bucle While se ejecuta mientras la condición (b<10) sea verdadera   
    
    print (b, end = ',')
    a, b = b, a + b