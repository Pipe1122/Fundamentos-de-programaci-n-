# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:34:35 2021

@author: Pipe
"""

# Programa que obtiene la calificación que debe obtenerse en un examen 
# supletorio, si se conoce que el promedio incluído el supletorio para aprobar
# debe ser mínimo 3.5. El usuario debe ingresar las calificaciones en números 
# enteros del primer y segundo bimestre.

# Entrada = Captura de datos
bimestre1 = float (input ("Ingrese su nota del bimestre 1:"))
bimestre2 = float (input ("Ingrese su nota del bimestre 2:"))


# Proceso = Realizar cálculos
nota = bimestre1 + bimestre2 / 2


# Salida = Imprimir resultados
if nota >= 3.5:
        print ("Aprobó.")
elif nota < 3.5:
        print ("No aprobó.")
        
supletorio = nota - 3.5
        

print ("La nota a obtener debe ser de:", supletorio)
