# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:43:09 2021

@author: Pipe
"""

'''
Programa que lee el nombre y la nota definitiva de tres materias (Basic, 
Fortran y Pascal) fr N estudiantes.                                                                
'''

# Declaración de variables
nombre = "***"
basic = 0.0
fortran = 0.0
pascal = 0.0
media = 0.0
cont_estudiantes = 0

# Leer el nombre
nombre = input("Digite el nombre del estudiante:")

# Ciclo While
while (nombre != "***"):    
# Inicio cilo    
    basic = float(input ("Definitiva Basic:"))
    fortran = float(input ("Definitiva Fortran:"))
    pascal = float(input ("Definitiva pascal:"))
    
# Procesos: Calculo de la media
    media = (basic + fortran + pascal) / 3
    print (f"La media es: {media:.1f}")
    nombre = input("Digite el nombre del estudiante:")
    cont_estudiantes = cont_estudiantes + 1
    
# Fin del ciclo 
print ("Cantidad de estudiantes:", cont_estudiantes)
print ("ADIOS...")
    