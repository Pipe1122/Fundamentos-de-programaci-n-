# -*- coding: utf-8 -*-
"""
Created on Thu May 13 19:01:01 2021

@author: Pipe
"""

# Crear estructuras de datos, hacer cálculos y graficar

# Declarar librerias para utilizar
import matplotlib.pyplot as plt

# Generar las listas con los datos inicializados
nombre_producto = ["Ron", "Aguardiente", "Vino", "Cerveza", "Tequila"]
cantidad_producto = [50, 70, 100, 200, 40]

# Funciones que resuelven el problema
def f_calc_total_cantidad():
    suma_cantidad = 0
    for poslis in range(4):
        suma_cantidad = suma_cantidad + cantidad_producto[poslis]
    print("Total cantidad", suma_cantidad)

def f_calc_total_cantidad_2():
    suma_cantidad = 0
    for poslis in range(4):
        suma_cantidad = suma_cantidad + cantidad_producto[poslis]
    return(suma_cantidad)

# Funcion que calcula el promedio de las cantidades
def f_calc_promedio():
    promedio = f_calc_total_cantidad_2() / len(cantidad_producto)
    return (promedio) 

# Llamado a las funciones que realizan los cálculos
f_calc_total_cantidad()
print("Total cantidad 2:", f_calc_total_cantidad_2())
print("Promedio cantidad:", f_calc_promedio())


# Graficar la informacion
fig, ax = plt.subplots()

# Definir el título del gráfico
ax.set_title("GRAFICO DE EXISTENCIAS DE PRODUCTOS")
ax.set_xlabel("Productos")
ax.set_ylabel("Cantidad")

# Crear el grafico
plt.bar(nombre_producto, cantidad_producto)

# Imprimir el grafico
plt.show()







