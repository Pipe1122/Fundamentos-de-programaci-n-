# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:53:27 2021

@author: Pipe
"""

# Programa para calcular la suma de los cuadrados de los primeros 100 números

# Variables
contador_repeticiones = 1
cuadrado_numero = 0
acumulador_suma = 0
cantidad_numeros = 0

# Entradas
cantidad_numeros = int (input("Cantidad de numeros:"))

# Ciclo While
while contador_repeticiones <= cantidad_numeros:
    cuadrado_numero = contador_repeticiones ** 2
    acumulador_suma = acumulador_suma + cuadrado_numero
    print("El cuadrado de:", contador_repeticiones, "es:", cuadrado_numero)
    print("La suma acumulada es:", acumulador_suma)
    contador_repeticiones = contador_repeticiones + 1
    # Fin del ciclo
    
# Salidas    
print("La suma de los cuadrados es:", acumulador_suma)
