# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:00:21 2021

@author: Pipe
"""

# Aplicación que solicita la carga de dos valores enteros y muestra la suma.
# Repetir la carga e impresión de la suma cinco veces.
# Mostrar una línea separadora después de que cargamos dos valores y su suma.

def carga_suma():
    valor1 = int(input("Ingrese el primer valor:"))
    valor2 = int(input("Ingrese el segundo valor"))
    suma = valor1 + valor2
    print("La suma de los dos valores es:", suma)
    
def separacion():
    print("*******************************")
    
# Programa principal

for x in range (5):
    carga_suma()
    separacion()
    
    
    