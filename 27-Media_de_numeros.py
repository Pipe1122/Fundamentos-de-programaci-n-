# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:52:09 2021

@author: Pipe
"""

# Determinar la media de una lista indefinida de numeros positivos terminados
# con un numero negativo

# Declaración de variables
num = 0 # Almacena los numeros que ingresa el usuario
suma = 0 # Suma los numeros que ingresa el usuario.
media = 0.0 # Saca la media de los numeros que ingresó el usuario.
cantidad_elementos = 0 # Almacena la cantidad de numeros digitados

num = int (input("Ingrese el numero:")) # Lectura del primer número

while (num > 0):
    suma = suma + num
    num = int (input("Ingrese el numero:"))
    cantidad_elementos = cantidad_elementos + 1
    # Termina el ciclo.

if cantidad_elementos != 0:
    media = suma / cantidad_elementos # Calcular la media
    print ("La media es:", media) # Imprimir la media
else:
    print ("No hay numeros para calcular la media")