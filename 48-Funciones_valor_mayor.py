# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:35:37 2021

@author: Pipe
"""

# Programa que recibe tres valores enteros y da el mayor de ellos.

def mostrar_mayor(v1, v2, v3):
    print("El valor mayor de los tres numeros es:")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)
            
def cargar():
    valor1 = int(input("Ingrese el primer valor:"))
    valor2 = int(input("Ingrese el segundo valor:"))
    valor3 = int(input("Ingrese el tercer valor:"))
    mostrar_mayor(valor1, valor2, valor3)
    
# Propuesta principal
cargar()

    