# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:39:53 2021

@author: Pipe
"""

# Leer numeros aleatorios y calcular suma y promedio

import random

# Variables
cantidad_numeros = 0
contador_repeticiones = 0
numero = 0
acumulador_suma = 0
promedio = 0.0

acumulador_negativos = 0
acumulador_positivos = 0
promedio_positivos = 0.0
promedio_negativos = 0.0
contador_negativos = 0
contador_positivos = 0

mayor_positivo = 0
mayor_negativo = 0
menor_positivo = 1000
menor_negativo = 0

#Entradas
cantidad_numeros = int(input("Cantidad de numeros:"))

#Procesos
# Inicio ciclo while
while contador_repeticiones < cantidad_numeros:
    numero = random.randint (-100, 100)
    acumulador_suma = acumulador_suma + numero
    
    if numero > 0: # Calculos para numeros positivos
        print("Numero positivo", numero)
        acumulador_positivos = acumulador_positivos + numero
        contador_positivos = contador_positivos + 1
        if numero > mayor_positivo: # Identificar mayor de los positivos
            mayor_positivo = numero
        if numero < menor_positivo: # Identificar menor de los positivos
            menor_positivo = numero
        
    else: # Calculo para numeros negativos
        print("Numero negativo", numero)
        acumulador_negativos = acumulador_negativos + numero
        contador_negativos = contador_negativos + 1  
        if numero > mayor_negativo:
            mayor_negativo = numero
        if numero < menor_negativo:
            menor_negativo = numero
    contador_repeticiones = contador_repeticiones + 1
    
# Fin del ciclo
promedio = acumulador_suma / contador_repeticiones
promedio_positivos = acumulador_positivos / contador_positivos
promedio_negativos = acumulador_negativos / contador_negativos
    
# Salidas de todos los numeros
print("La suma de los numeros es:", acumulador_suma)
print("El promedio de los numeros es:", promedio)

# Salidas de los numero positivos
print("Cantidad de numeros positivos:", contador_positivos)
print("La suma de los numeros postivos:", acumulador_positivos)
print("Promedio de numeros positivos:", promedio_positivos)

# Salidas de los numeros negativos
print("Cantidad de numeros negativos:", acumulador_negativos)
print("La suma de los negativos es:", acumulador_negativos)
print("El promedio de los numeros negativos es:", promedio_negativos)

# Salidas del nayor y menor de los positivos
print("El numero mayor de los positivos es:", mayor_positivo)
print("El numero menor de los positivos es:", menor_positivo)

# Salidas del mayor y menor de los negativos
print("El numero mayor de los negativos es:", mayor_negativo)
print("El numero menor de los negativos es:", menor_negativo)
    
    
    
    