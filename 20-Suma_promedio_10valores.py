# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:22:42 2021

@author: Pipe
"""

# Desarrollar un programa que permita la carga de 10 valores por teclado y 
# nos muestre posteriormente la suma de los valores ingresados y su promedio.

suma = 0
for i in range(10):
    valor = int(input("Ingrese el valor:"))
    suma = suma + valor
print("La suma es", suma)
promedio = suma / 10
print("El promedio es:", promedio)
