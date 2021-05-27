# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:43:21 2021

@author: Pipe
"""

# Programa que realiza lo siguiente: Si n empleados realizan una actividad
# en k horas, ¿Cuántos empleados se necesitan para realizar la misma actividad 
# en k1 horas?

import math
# Entradas.
k_hrs = int (input("Ingrese las horas que tardan realizando la actividad:"))
n = int (input("Ingrese el numero de empleados:"))
k1_hrs = int (input("Ingrese las horas en las que se debe hacer la actividad:"))

# Procesos.
empleados = n * (k_hrs / k1_hrs)

# Salidas.
r = math.ceil(empleados)
print ("La cantidad de empleados para realizar la actividad debe ser de:", r)