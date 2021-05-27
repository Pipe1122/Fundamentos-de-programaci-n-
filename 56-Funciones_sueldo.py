# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:42:15 2021

@author: Pipe
"""

# Función que reciba el nombre de un operario, el pago por hora y la cantidad 
# de horas trabajadas. Debe mostrar su sueldo y el nombre. Hacer la llamada 
# de la función mediante argumentos nombrados.

def calcular_sueldo(nombre, costo_hora, cantidad_horas):
    sueldo = costo_hora * cantidad_horas
    print(nombre,"trabajo",cantidad_horas,"y cobra un sueldo de",sueldo)
    
# Bloque principal
calcular_sueldo("Juan", 10, 120)
calcular_sueldo(costo_hora = 12, cantidad_horas = 40, nombre = "Laura")
calcular_sueldo(cantidad_horas = 90, nombre = "Felipe", costo_hora = 7)


