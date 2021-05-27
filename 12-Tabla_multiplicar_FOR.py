# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:36:27 2021

@author: Pipe
"""

# Leer una tabla de multiplicar e imprimirla desde el 1 hasta el 20, y sumar 
# con sus resultados. Utilizar: Ciclo For.

# Declarar variables
tabla = 0
multiplicador = 1
resultado = 0
suma_resultado = 0
contador_repeticion_ciclo = 1

# Leer el número de la tabla para la cual se van a realizar las operaciones
tabla = int (input("Tabla:"))

# Leer el multiplicador
multiplicador = int (input("Multiplicador:"))

# Inicio del ciclo FOR.
for contador_repeticion_ciclo in range (multiplicador + 1):
    resultado = tabla * contador_repeticion_ciclo
    suma_resultado = suma_resultado + resultado
    print (tabla, "*", contador_repeticion_ciclo, "=", resultado)
    
    # Incrementar la variable que controla el ciclo
# Se imprime la suma por fuera del ciclo 
print ("La suma de los resultados es:", suma_resultado)