# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:03:34 2021

@author: Pipe
"""

# Una planta que fabrica perfiles de hierro posee un lote de n piezas.
# Confeccionar un programa que pida ingresar por teclado la cantidad de piezas 
# a procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza 
# cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. 
# Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.

cantidad = 0
x = 1

n = int(input("¿Cuantas piezas va a cargar?:"))
while x<=n:
    largo = float(input("Ingrese la medida de la pieza:"))
    if largo >= 1.2 and largo >= 1.3:
        cantidad = cantidad + 1
    x = x + 1
print("La cantidad de piezas aptas son:", cantidad)