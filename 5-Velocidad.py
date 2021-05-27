# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 23:05:54 2021

@author: Pipe
"""

# Calcular la velocidad a la que debe ir un vehículo para recorrer una 
# distancia d en un tiempo t.

# Entrada = Captura de datos
distancia = int (input ("Ingrese la distancia a recorrer en Km:"))
tiempo = int (input("Ingrese el tiempo en horas en el cual se hara el recorrido:"))


# Proceso = Realizar cálculos
velocidad = distancia / tiempo


# Salida = Imprimir resultado
print ("La velocidad a la que debe ir el vehiculo en Km/h debe ser de:", velocidad)