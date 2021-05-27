# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:49:26 2021

@author: Pipe
"""

# Imprimir las treinta primeras potencias de 10, es decir, 10 elevado a 1, 10 
# elevado a 2, etc. además sumar las potencias calculadas

suma = 0

for i in range(1, 31):
    potencia = 10 ** i
    print(potencia)
    suma = suma + potencia
    
print("La suma de las potencias es:", suma)


    
    