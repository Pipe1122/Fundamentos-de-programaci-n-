# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:46:29 2021

@author: Pipe
"""

# Aplicacion que muestra una presentacion en pantalla del programa.
# El usuario solicita la carga de dos valores y nos muestra la suma. 
# Al final se mostrará un mensaje de despedida, se deben hacer 3 funciones.

def presentacion():
    print("Programa que permite cargar dos valores por teclado.")
    print("Efectua la suma de los valores.")
    print("Muestra el resultado de la suma.")
    print("********************************")
    
def carga_suma():
    valor1 = int(input ("Ingrese el primer valor:"))
    valor2 = int(input ("Ingrese el segundo valor:"))
    suma = valor1 + valor2
    print("La suma de los valores es:", suma)
    
def finalizacion():
    print("********************************")
    print("Gracias por utilizar el programa.")
    
# Programa principal

presentacion()
carga_suma()
finalizacion()    
