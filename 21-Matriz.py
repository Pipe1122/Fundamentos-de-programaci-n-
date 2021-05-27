# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:21:05 2021

@author: Pipe
"""

matriz_numeros =  [[7,8,3], [1,9,2], [4,6,5]]
print(matriz_numeros)

# Suma de los elementos de la matriz
suma_elementos = 0
for f in range(3):
    for c in range(3):
        suma_elementos = suma_elementos + matriz_numeros[f][c]
print("La suma de los elementos es:", suma_elementos)     

# Imprimir la matriz
for f in range(3):
    for c in range(3):
        print("Dato", matriz_numeros[f][c])
   
# Sumar la diagonal principal
suma_diagonal = 0
for pos in range(3):
    suma_diagonal = suma_diagonal + matriz_numeros[pos][pos]
print("Diagonal principal:", suma_diagonal)