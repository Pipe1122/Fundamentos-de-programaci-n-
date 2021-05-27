# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:22:58 2021

@author: Pipe
"""

# Calcular el valor a pagar de una compra realizada, cuyo monto neto es 
# ingresado por el usuario. Considere que el valor del IVA (Impuesto al valor
# agregado - puede variar en cada país) y un descuento del 5% para todas las
# compras.



# Entrada = Captura de datos
valor = int (input ("Ingrese el valor del producto:"))
descuento = valor * 0.05
iva = valor * 0.19


# Proceso = Realizar cálculos
total = valor - descuento + iva 


# Salida = Imprimir resultados
print ("El total a pagar es:", total)


