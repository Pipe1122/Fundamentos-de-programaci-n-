# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:50:47 2021

@author: Pipe
"""

# Leer una tabla de multiplicar e imprimirla desde el 1 hasta el 20, y sumar 
# con sus resultados. Utilizar: Ciclo While.

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

# Inicio del ciclo repetitivo WHILE.
while (contador_repeticion_ciclo <= multiplicador):
    resultado = tabla * contador_repeticion_ciclo
    suma_resultado = suma_resultado + resultado
    print (tabla, "*", contador_repeticion_ciclo, "=", resultado)
    
    # Incrementar la variable que controla el ciclo
    contador_repeticion_ciclo = contador_repeticion_ciclo + 1
print ("La suma de los resultados es:", suma_resultado)