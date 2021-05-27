# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:20:03 2021

@author: Pipe
"""

# Calcular la fuerza que se debe aplicar a un cuerpo para moverlo en una mesa
# horizontal, sabiendo que tiene una masa m (kg) y un coeficiente de 
# rozamiento estático us.

# Entradas
gravedad = 9.8
masa = float(input("Ingrese la masa en Kg:"))
cre = float(input("Ingrese el coeficiente de rozamiento estatico:"))

# Procesos
fuerza_normal = masa * gravedad
fuerza_rozamiento = cre * fuerza_normal

# Salidas
print("La fuerza de rozamiento es:", fuerza_rozamiento)