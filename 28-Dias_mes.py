# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 12:03:47 2021

@author: Pipe
"""

# Dado el nombre de un mes y si el año es o no bisiesto, deducir el número
# de días del mes.

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = input("Ingrese el mes:").lower()
año = int(input("Ingrese el año:"))

for i in range(12):
    if mes == meses[i]:
        if i == 1 and (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
            print(dias_mes[i] + 1)
        else:
            print(dias_mes[i])
            
            