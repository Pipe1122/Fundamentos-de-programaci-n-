# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:04:06 2021

@author: Pipe
"""

# Calcular el área y perímetro de un rectángulo.

# Entradas
base = float(input("Ingrese la base del rectangulo:"))
altura = float(input("Ingrese la altura del rectangulo:"))
 
# Procesos
area = base * altura
perimetro = (base + altura) * 2

# Salidas
print("El area del rectangulo es:", area)
print("El perimetro del rectangulo es:", perimetro)