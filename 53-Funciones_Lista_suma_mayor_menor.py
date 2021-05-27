# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:19:24 2021

@author: Pipe
"""

# Definir por asignación una lista de enteros en el bloque principal 
# del programa. Elaborar tres funciones, la primera recibe la lista y retorna 
# la suma de todos sus elementos, la segunda recibe la lista y retorna 
# el mayor valor y la última recibe la lista y retorna el menor.

def sumarizar(lista):
    suma = 0
    for x in range (len(lista)):
        suma = suma + lista [x]
    return suma

def mayor(lista):
    mayor = lista [0]
    for x in range (1, len(lista)):
        if lista [x]>mayor:
            mayor = lista [x]
    return mayor

def menor(lista):
    menor = lista [0]
    for x in range (1, len (lista)):
        if lista [x]<menor:
            menor = lista[x]
    return menor

# Bloque principal del programa
lista_valores = [10, 56, 23, 120, 94]
print("La lista completa es:")
print(lista_valores)
print("La suma de todos su elementos es", sumarizar(lista_valores))
print("El mayor valor de la lista es", mayor(lista_valores))
print("El menor valor de la lista es", menor(lista_valores))


    