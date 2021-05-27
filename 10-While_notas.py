# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:42:42 2021

@author: Pipe
"""

# Porgrama que calcula la nota de un estudiante

# Entradas
# Pedir la cantidad y el nombre del estudiante y sus tres notas de parciales.

cant_est = int (input ("Cantidad de estudiantes:"))

# Inicializar la variable que controla el ciclo.
conRep = 0

# Variable real para sumar la definitiva del grupo
suma_def_grupo = 0.0

# Variable para calcular la nota promedio del grupo.
promedio_grupo = 0.0 

while (conRep < cant_est):
    # Instrucciones a repetir
    nombre = input ("Nombre del estudiante:")
    not1 = float(input ("Primer parcial:"))
    not2 = float(input ("Segudno parcial:"))
    not3 = float(input ("Tercer parcial:"))

    # Cálculos
    definitiva = (not1 + not2 + not3) / 3
    
    # Acumulo las definitivas del grupo.
    suma_def_grupo = suma_def_grupo + definitiva

    # Salida: Imprimir resultados
    print (f"1. La nota definitiva es: {definitiva:.2f} ")
    
    # Incrementar la variable que contola el ciclo 
    conRep = conRep+1

# Calcular el promedio del grupo
promedio_grupo = suma_def_grupo + cant_est

# Imprimir la nota promedio del grupo
print (f"2. La nota promedio del grupo es: {promedio_grupo:.2f}")




