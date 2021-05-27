# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:30:58 2021

@author: Pipe
"""

# Arreglos-vectores
# Almacenar en un vector las 5 notas del parcial

# Declarar el vector (LISTA)
lista_notas = []
suma_notas = 0.0

# Valores de la lista con un ciclo
for pos_lista in range(5):
    # Leer la nota desde teclado
    nota_estudiante = float(input("Digite su nota:"))
    suma_notas = suma_notas + nota_estudiante
    # Almacenar el escalar en el arreglo
    lista_notas.append(nota_estudiante)
    
#Imprimir el arreglo
print(lista_notas)
print("La suma de las notas es:", suma_notas)
    

