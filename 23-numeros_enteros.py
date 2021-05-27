# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 21:57:53 2021

@author: Pipe
"""

print("ingrese 3 numeros enteros diferenetes") 
# El usuario debe ingresar los números enteros (Diferentes)


a = int(input("ingrese el numero a"))
# El usuario debe asignar un valor a la variable a.

b = int(input("ingrese el numero b"))
# El usuario debe asignar un valor a la variable b.

c = int(input("ingrese el numero c"))
# El usuario debe asignar un valor a la variable c.

e = int(input("elija 1 si lo quiere de mayor a menor y 2 si lo quiere de menor a mayor"))
# El usuario elige 1 o 2, dependiendo su necesidad.

if (e == 1):    
# En esta condición se indica que "e" es igual a 1.

    if (a > b):
# En esta condición se indica que "a" es mayor que "b".

        if (a > c):
# En esta condición se indica que "a" es mayor que "c".

            if(b > c):
# En esta condición se indica que "b" es mayor que "c".
                
               print(a, b, c)
# En este paso se indica que la consola muestre los valores asignados a "a", "b" y "c" en el siguiente orden: a,b,c
               
            else:
# Indica que si no se cumple la anterior condición, se debe hacer otro proceso.

               print(a, c, b)
# En este paso se indica que la consola muestre los valores asignados a "a", "b" y "c" en el siguiente orden: a,c,b

    if (c > a):
# Esta condición indica que "c" es mayor que "a".
        
        if (c > b):
# Esta condición indica que "c" es mayor que "b".

            if(b > a):
# Esta condición indica que "b" es mayor que "a".

               print(c, b, a)
# En este paso se indica que la consola muestre los valores asignados a "a", "b" y "c" en el siguiente orden: c,b,a

            else:
# Indica que si no se cumple la anterior condición, se debe hacer otro proceso.

               print(c, a, b)
# En este paso se indica que la consola muestre los valores asignados a "a", "b" y "c" en el siguiente orden: c,a,b

    if (b > a):
# Esta condición indica que "b" es mayor que "a".

        if (b > c):
# Esta condición indica que "b" es mayor que "c".
            
            if(a > c):
# Esta condición indica que "a" es mayor que "c".
                
               print(b, a, c)
# En este paso se indica que la consola muestre los valores asignados a "a", "b" y "c" en el siguiente orden: b,a,c
               
            else:
# Indica que si no se cumple la anterior condición, se debe hacer otro proceso.

               print(b, c, a)
# En este paso se indica que la consola muestre los valores asignados a "a", "b" y "c" en el siguiente orden: b,c,a

if (e == 2):
# Esta condición indica que la variable "e" es igual a 2.    

    if (a < b):
# Esta condición indica que "a" es menor que "b".
        
        if (a < c):
# Esta condición indica que "a" es menor que "c".
        
            if(b < c):
# Esta condición indica que "b" es menor que "c".

               print(a, b, c)
# En este paso se indica que la consola muestre los valores asignados a "a", "b" y "c" en el siguiente orden: a, b, c 
             
            else:
# Indica que si no se cumple la anterior condición, se debe hacer otro proceso.         
    
               print(a, c, b)
# En este paso se indica que la consola muestre los valores asignados a "a", "b" y "c" en el siguiente orden: a, c, b

    if (c < a):
# Esta condición indica que "c" es menor que "a".
        
        if (c < b):
# Esta condición indica que "c" es menor que "b".
            
            if(b < a):
# Esta condición indica que "b" es menor que "a".
                
               print(c, b, a)
# En este paso se indica que la consola muestre los valores asignados a "a", "b" y "c" en el siguiente orden: c, b, a
               
            else:
# Indica que si no se cumple la anterior condición, se debe hacer otro proceso.  
                
               print(c, a, b)
# En este paso se indica que la consola muestre los valores asignador a "a", "b" y "c" en el siguiente orden: c, a, b
               
    if (b < a):
# Esta condición indica que "b" es menor que "a".
        
        if (b < c):
# Esta condición indica que "b" es menor que "c".
            
            if(a < c):
# Esta condición indica que "a" es menor que "c".
                
               print(b, a, c)
# En este paso se indica que la consola muestre los valores asignador a "a", "b" y "c" en el siguiente orden: b, a, c
               
            else:
# Indica que si no se cumple la anterior condición, se debe hacer otro proceso.
                
               print(b, c, a)
# En este paso se indica que la consola muestre los valores asignador a "a", "b" y "c" en el siguiente orden: b, c, a

if (a == b):
# Esta condición indica que "a" es igual a "b"
    
    print("b y a son iguales")
# Se utiliza para mostrar en la consola que "b" y "a" son iguales.
    
    if (a == c):
# Esta condición indica que "a" y "c" son iguales.
        
        print("a y c son iguales")
# Se utiliza para mostrar en la consola que "a" y "c" son iguales.

        if(b == c):
# Esta condición indica que "b" y "c" son iguales.
            
           print(" b y c con iguales")
# Se utiliza para mostrar en la consola que "b" y "c" son iguales.

           if(a == b == c):
# Esta condición indica que las tres variables (a, b, c) son iguales.
               
              print("todos son iguales")
# Muestra en la consola que las todas las variables son iguales.