# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:49:41 2021

@author: Pipe
"""

# Programa que obtiene el índice de masa corporal de una persona, ingresando
# la estatura en cm y el peso en kg.

# Entrada = Captura de datos
estatura = int (input ("¿Cuanto mides?:"))
peso = int (input ("¿Cuanto pesas?"))


# Proceso = Realizar cálculos
altura_en_mts = estatura / 100
imc = peso / altura_en_mts ** 2


# Salida = Imprimir resultados
print ("Su indice de masa corporal es:", imc)
