# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:21:34 2021

@author: Pipe
"""

# Calcular el sueldo total a recibir de un empleado. El usuario deberá ingresar
# el numero de horas trabajadas y el valor por cada hora. Considere en los 
# cálculos el descuento de seguridad social y una bonificación del 2% para 
# aquellos cuyo sueldo no supere los 300 dólares.

# Entradas
seguridad = 0.07
bonificacion = 0.2
horas_trabajadas = float(input("Ingrese el numero de horas trabajadas:"))
valor_hora = float(input("Ingrese el valor de la hora:"))

# Procesos
sueldo = horas_trabajadas * valor_hora
sueldo_seguridad = sueldo - sueldo*seguridad
sueldoT = sueldo * bonificacion

if sueldo <= 300:
    total = sueldo_seguridad + sueldoT
    print("El sueldo mas la bonificacion es de:", total)
else:
    print("El sueldo es de:", sueldo_seguridad)



