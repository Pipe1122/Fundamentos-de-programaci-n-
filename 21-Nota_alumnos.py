# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:29:39 2021

@author: Pipe
"""

# Escribir un programa que solicite por teclado 10 notas de alumnos y nos 
# informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

aprobados = 0
reprobados = 0

for i in range(10):
    nota = int(input("Ingrese la nota:"))
    if nota >=7:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1
print("Cantidad de aprobados", aprobados)
print("Cantidad de reprobados:", reprobados)

    