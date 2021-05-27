# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:47:18 2021

@author: Pipe
"""

# Variables escalares
print("VARIABLE ESCALAR")
VarEscNum = 10
print(VarEscNum)
VarEscNum = 20 
print(VarEscNum)
print()

# Variables vectoriales - N datos del mismo tipo de datos
# Aplicación de estructuras de datos
print("ARREGLO VECTORIAL")
vector_numero = [10, 20, 30, 40]
print(vector_numero)

# Funciones de una lista.
# Adicionar al final de la lista
vector_numero.append(2000)
print(vector_numero)
print()

# Adicionar datos por teclado a una lista
vector_numero_teclado1 = []
#Adicionar datos mediante un ciclo
for pos in range(3):
    dato_teclado = int(input("Digite el el valor:")) # Escalar
    vector_numero_teclado1.append(dato_teclado)
    
print(vector_numero_teclado1)
vector_numero_teclado1.append(3000)
print(vector_numero_teclado1)

# Borrar los elementos de la lista
# vector_numero_teclado1.clear()

# Crear una nueva lista con sus datos
vector_numero2 = [2, 4, 6, 8, 10]
print(vector_numero_teclado1)
print(vector_numero2)

# Unir listas
vector_numero_teclado1.extend(vector_numero2)
print(vector_numero_teclado1)

# Conocer el tamaño de la lista
tamaño_vector = len(vector_numero_teclado1)
print("tamaño:", tamaño_vector)

# Contar las repeticiones de un dato
print(vector_numero_teclado1.count(12))















    