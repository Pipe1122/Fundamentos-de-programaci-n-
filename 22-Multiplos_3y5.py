# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:34:50 2021

@author: Pipe
"""

# Escribir un programa que lea 10 números enteros y luego muestre cuántos 
# valores ingresados fueron múltiplos de 3 y cuántos de 5. Debemos tener en 
# cuenta que hay números que son múltiplos de 3 y de 5 a la vez.

multiplo3 = 0
multiplo5 = 5

for f in range(10):
    valor = int(input("Ingrese un valor:"))
    if valor %3 == 0:
        multiplo3 = multiplo3 + 1
    if valor %5 == 0:
        multiplo5 = multiplo5 + 1

print("Cantidad de valores ingresados multiplos de 3:")
print(multiplo3)
print("Cantidad de valores ingresados multiplos de 5:")
print(multiplo5)
