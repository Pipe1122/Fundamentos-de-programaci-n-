# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:22:04 2021

@author: Pipe
"""

# Leer la temperatura en grados Celsius y convertirla a grados Kelvin y a 
# grados Farenheit.

# Entradas.
celsius = float (input("Ingrese la temperatura en °C:"))


# Procesos.
kelvin = celsius + 273.15
farenheit = (celsius * 1.8) + 32

# Salidas
print ("La temperatura en °K es de:", kelvin)
print ("La temperatura en °F es de:", farenheit)
