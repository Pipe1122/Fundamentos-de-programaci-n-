# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:42:24 2021

@author: Pipe
"""

# Programa que permita ingresar el lado de un cuadrado. 
# Pregunta si se quiere calcular su perímetro o superficie

def mostrar_perimetro(lado):
    perimetro = lado * 4
    print("El perimetro es:", perimetro)
    
def mostrar_superficie(lado):
    superficie = lado * lado
    print("La superficie es:", superficie)

def cargar_datos():
    lado = int(input("Ingrese el valor del lado de un cuadrado:"))
    respuesta = input("¿Quiere calcular el perimetro o la superficie? [ingrese texto: perimetro/superficie]?")
    if respuesta == "perimetro":
        mostrar_perimetro(lado)
    if respuesta == "superficie":
        mostrar_superficie(lado)
        
# Programa principal 
cargar_datos()


