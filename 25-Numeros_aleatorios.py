# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:12:59 2021

@author: Pipe
"""

# Programa que genera aleatoriamente 100 datos y haga los siguientes procesos:
# 1. Suma los números
# 2. Sume los números negativos
# 3. Sume los números positivos
# 4. Calcular el promedio de todos los números
# 5. Calcular el promedio de los números positivos.
# 6. Calcular el promedio de los números negativos
# 7. Calcular el mayor de todos los números
# 8. Calcular el menor de todos los números

import random

# Variables
contador_repeticiones = 0
acumulador_sumat = 0 
acumulador_sumap = 0
acumulador_suman = 0
numero = 0
cantidad_numeros = 1

# Entradas
cantidad_numeros = int (input("Ingrese la cantidad de numeros:"))

# Incio del ciclo While
while contador_repeticiones < cantidad_numeros:
    numero = random.randint(-50, 50)
    print("numero", numero)
    acumulador_sumat = acumulador_sumat + numero
    if numero > 0:
        acumulador_sumap = acumulador_sumap + numero
    else:
        acumulador_suman = acumulador_suman + numero
    contador_repeticiones = contador_repeticiones + 1
# Fin del ciclo

# Salida
print("La suma de todos los numeros es:", acumulador_sumat)
print("La suma de los numeros positivos es:", acumulador_sumap)
print("La suma de los numeros negativos es:", acumulador_suman)

    