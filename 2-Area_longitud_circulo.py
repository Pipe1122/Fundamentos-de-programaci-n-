# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 12:06:23 2021

@author: Pipe
"""

# Calcular el área de un círculo y longiud de su circunferencia.

# Entrada = Captura de datos
pi = 3.1416
radio = int (input ("Ingrese el radio de la circunferencia:"))

# Procesos = Realizar cálculos
area = pi * radio ** 2
longitud = 2 * pi * radio


# Salidas = Imprimir resultados
print ("El area de la circunferencia es de:", area)
print ("La longitud de la circunferencia es:", longitud)