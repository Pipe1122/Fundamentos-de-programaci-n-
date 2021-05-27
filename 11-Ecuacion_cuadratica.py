# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:18:35 2021

@author: Pipe
"""

# Calcular las raices de una ecuación cuadrática, suponiendo que los datos
# no generan raices imaginarias.

import math
# Entradas
a = float(input("Ingrese el valor de a:"))
b = float(input("Ingrese el valor de b:"))
c = float(input("Ingrese el valor de c:"))

# Procesos
x1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a


# Salidas
print("El valor de X1 es:", x1)
print("El valor de X2 es:", x2)
