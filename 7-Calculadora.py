# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:07:44 2021

@author: Pipe
"""

# Programa que simula una calculadora básica, con las operaciones: suma, resta
# multiplicación, división y potencia.

import math
while True:

    print ("Menu:")
    print ("1.Suma")
    print ("2.Resta")
    print ("3.Multiplicacion")
    print ("4.Division")
    print ("5.Potencia")
    print ("6.Salir")

    opcion = int (input("ingrese operación a realizar: "))

    if opcion == 6:
        break
    
    num1 = float (input("Ingrese numero 1: "))
    num2 = float (input("ingrese numero 2: "))

    if opcion == 1:
        suma = num1 + num2
        print("La suma es:", suma)
    elif opcion == 2:
        resta = num1 - num2
        print("La resta es:", resta)
    elif opcion == 3:
        multiplicacion = num1 * num2
        print("La multiplicacion es:", multiplicacion)
    elif opcion == 4:
        division = num1 / num2
        print("La division es:", division)
    elif opcion == 5:
        potencia = math.pow(num1, num2)
        print("La potencia es:", potencia)
        


