# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:28:45 2021

@author: Pipe
"""

# Crear y cargar  una lista de 5 enteros. Implementar una función que imprima 
# el mayor y el menor valor de la lista.

def mayor_menor(lista):
    mayor = lista [0]
    menor = lista [0]
    for x in range (1, len(lista)):
        if lista [x]>mayor:
            mayor = lista [x]
        else:
            if lista [x]<menor:
                menor = lista [x]
    print("El valor mayor de la lista es:", mayor)
    print("El valor menor de la lista es:", menor)
    
# Bloque principal
lista = []
for x in range (5):
    valor = int(input("Ingrese valor:"))
    lista.append(valor)
mayor_menor(lista)