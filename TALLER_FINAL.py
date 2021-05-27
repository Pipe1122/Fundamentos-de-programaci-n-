# -*- coding: utf-8 -*-
"""
Created on Tue May 25 19:31:19 2021

@author: Pipe
"""

import pandas as pd
import matplotlib.pyplot as plt

#LEER EL EXCEL
df_archivoex = pd.read_excel('Futbol_Partidos.xlsx')


# EJERCICIO 1
# CANTIDAD DE GOLES DE LOS EQUIPOS LOCALES
def ejercicio_1():
    equipos_locales = df_archivoex['local'].unique()
    #print(equipos_locales)
    def f_goles_locales(equipos_locales):
        goles=[]
        for equipo in equipos_locales:
          filtro = df_archivoex[df_archivoex['local'] == equipo]
          goles_equipo= filtro['goles_local'].sum()
          goles.append(filtro['goles_local'].sum())
          print(equipo, "goles",goles_equipo) 
          #print(goles)  
        return goles
    
    goles_locales_x_equipo = f_goles_locales(equipos_locales)
    suma_goles_locales1 = df_archivoex['goles_local'].sum()
    print("El total de goles locales es:", suma_goles_locales1)
    
    def graficar(equipos_locales, goles_locales_x_equipo):
        fig,ax = plt.subplots()
        ax.set_title('GOLES LOCAL POR EQUIPO')
        ax.set_xlabel('Equipo')
        ax.set_ylabel("Goles")
        plt.barh(equipos_locales, goles_locales_x_equipo)
        plt.show()
    
    graficar(equipos_locales, goles_locales_x_equipo)
    print()

# EJERCICIO 2
# CANTIDAD DE GOLES DE LOS EQUIPOS VISITANTES
def ejercicio_2():
    equipos_visitantes = df_archivoex['visitante'].unique()
    #print(equipos_visitantes)
    
    def f_goles_visitantes(equipos_visitantes):
        goles=[]
        for equipo in equipos_visitantes:
          filtro = df_archivoex[df_archivoex['visitante'] == equipo]
          goles_equipo= filtro['goles_visita'].sum()
          goles.append(filtro['goles_visita'].sum())
          print(equipo, "goles",goles_equipo)   
        return goles
    
    goles_visitantes_x_equipo = f_goles_visitantes(equipos_visitantes)
    
    def graficar(equipos_visitantes, goles_locales_x_equipo):
        fig,ax = plt.subplots()
        ax.set_title('GOLES VISITANTES POR EQUIPO')
        ax.set_xlabel('Equipo')
        ax.set_ylabel("Goles")
        plt.barh(equipos_visitantes, goles_visitantes_x_equipo)
        plt.show()
    
    print()
    graficar(equipos_visitantes, goles_visitantes_x_equipo)
    print()

# EJERCICIO 3
# CANTIDAD TOTAL DE GOLES DE TODOS LOS PARTIDOS
def ejercicio_3():
    def total_goles():    
        suma_goles_locales = df_archivoex['goles_local'].sum()
        suma_goles_visitante = df_archivoex['goles_visita'].sum()
        print('Goles local= ',suma_goles_locales,"Goles visita=",suma_goles_visitante )
    
        suma_total = suma_goles_locales + suma_goles_visitante
        print("Goles totales:", suma_total)
        print()
        def graficar(suma_total):
            fig,ax = plt.subplots()
            ax.set_title('Goles Todos los Partidos')
            ax.set_ylabel("Goles")
            plt.bar(["total"], suma_total)
            plt.show()
        graficar(suma_total)
    print(total_goles())

# EJERCICIO 4 
# CANTIDAD DE GOLES DE LOS EQUIPOS LOCALES POR CAMPEONATO
# Arreglo de los torneos
def ejercicio_4():
    torneos = df_archivoex['torneo'].unique()
    
    # grafica las estadísticas de goles de los equipos locales
    # en cada torneo
    def draw(torneos, goles_torneos):
        fig,ax = plt.subplots()
        ax.set_title('GOLES POR TORNEO DE LOS EQUIPOS LOCALES')
        ax.set_xlabel('CANTIDAD')
        ax.set_ylabel("TORNEO")
        plt.barh(torneos, goles_torneos)
        plt.show()  
    # Retorna un arreglo que contiene los goles marcados en cada torneo
    def get_goles(torneos):
        goles = []
        for t in torneos:
            torneo = df_archivoex[df_archivoex['torneo'] == t]
            goles.append(torneo['goles_local'].sum())
        return goles    
    # Goles de los torneos
    goles_torneos = get_goles(torneos)
    print("Los torneos son:")
    print(torneos)
    print()
    print("Los goles marcados por los equipos locales fueron:", goles_torneos)

    # gráfica
    draw(torneos, goles_torneos)

# EJERCICIO 5
# CANTIDAD DE GOLES DE LOS EQUIPOS VISITANTES POR CAMPEONATO
def ejercicio_5():
    torneos2 = df_archivoex['torneo'].unique()
    torneos2
    
    # grafica las estadísticas de goles de los equipos locales
    # en cada torneo
    def draw(torneos2, goles_torneos):
        fig,ax = plt.subplots()
        ax.set_title('GOLES POR TORNEO DE LOS EQUIPOS VISITANTES')
        ax.set_xlabel('CANTIDAD')
        ax.set_ylabel("TORNEO")
        plt.barh(torneos2, goles_torneos)
        plt.show()  
    # Retorna un arreglo que contiene los goles marcados en cada torneo
    def get_goles2(torneos2):
        goles2 = []
        for t in torneos2:
            torneo = df_archivoex[df_archivoex['torneo'] == t]
            goles2.append(torneo['goles_visita'].sum())
        return goles2    
    # Goles de los torneos
    print()
    goles_torneos = get_goles2(torneos2)
    print()
    print("Los goles marcados por los visitantes fueron:", goles_torneos)
    
    # gráfica
    draw(torneos2, goles_torneos)

#EJERCICIO 6 
#TOTAL DE GOLES POR CAMPEONATO 
def ejercicio_6():
    campeonatos=df_archivoex['torneo'].unique()
    golestotales=[]
    cantidadgolesl=[]
    cantidadgolesv=[]
    for golest in campeonatos:
        cantidadgolesl=df_archivoex[df_archivoex['torneo']==golest].goles_local.sum()
        cantidadgolesv=df_archivoex[df_archivoex['torneo']==golest].goles_visita.sum()
        cantidadgolest=cantidadgolesl+cantidadgolesv
        golestotales.append(cantidadgolest)
        print(golest,cantidadgolest)
      
              
    fig,ax =plt.subplots()
    ax.set_title("Goles totales por torneos ")
    ax.set_ylabel("Torneo")
    ax.set_xlabel("Cantidad de Goles")
    plt.barh(campeonatos,golestotales)
    plt.show()
                          
#EJERCICIO 7 
#GRAFICO CANTIDAD DE PARTIDOS POR SELECCIÓN
def ejercicio_7():
    equipos =df_archivoex['local'].value_counts()
    equipos2=df_archivoex['visitante'].value_counts()
    total=equipos+equipos2
    print(total)
    
    #GRAFICA
    fig,ax = plt.subplots()
    ax.set_title('CANTIDAD DE PARTIDOS POR SELECCION')
    ax.set_xlabel('SELECCION')
    ax.set_ylabel("# PARTIDOS")
    total.plot(kind = 'bar', width=0.7)
    plt.show()

#EJERCICIO 9
#SELECCIÓN QUE MAS GOLES REALIZO EN TODOS LOS CAMPEONATOS
def ejercicio_9():
    equipos = df_archivoex['local'].unique()

    def f_equipo_con_mas_goles(equipos):
      #Se crea diccionario python con {}
        goles={}
        for equipo in equipos:
          #Suma goles como local
          filtro_local = df_archivoex[df_archivoex['local'] == equipo]
          goles_como_local= filtro_local['goles_local'].sum()
          #Suma goles como visitante
          filtro_visitante= df_archivoex[df_archivoex['visitante'] == equipo]
          goles_como_visitante=filtro_visitante['goles_visita'].sum()
          #Suma local + visitante
          total_goles_equipo = goles_como_local + goles_como_visitante
          #Se agregan los valores al diccionario {equipo:total_goles_equipo}
          goles[equipo] = total_goles_equipo
          
          #Se selecciona el valor mas alto en el diccionario
          #para usar esto se importó "operator"
          equipo_con_mas_goles = max(goles, key = goles.get)
        print(goles)
        print("Selección que mas goles realizo en todos los campeonatos : ",equipo_con_mas_goles)    
     
    
    f_equipo_con_mas_goles(equipos)


#EJERCICIO 10
#SELECCIÓN QUE MAS GOLES RECIBIO EN TODOS LOS CAMPEONATOS
def ejercicio_10():
    equipos = df_archivoex['local'].unique()
    
    def f_equipo_recibiog(equipos):
      #Se crea diccionario con python
        goles={}
        for equipo in equipos:
          #Suma goles como local
          filtro_local = df_archivoex[df_archivoex['local'] == equipo]
          goles_como_local= filtro_local['goles_visita'].sum()
          #Suma goles como visitante
          filtro_visitante= df_archivoex[df_archivoex['visitante'] == equipo]
          goles_como_visitante=filtro_visitante['goles_local'].sum()
          #Suma local + visitante
          total_goles_equipo = goles_como_local + goles_como_visitante
          #Se agregan los valores al diccionario {equipo:total_goles_equipo}
          goles[equipo] = total_goles_equipo
          
          #Se selecciona el valor mas alto en el diccionario
          #para usar esto se importó "operator"
          equipo_con_mas_goles = max(goles, key = goles.get)
        print()
        print(goles)
        print()
        print("SELECCIÓN QUE MAS GOLES RECIBIO EN LOS CAMPEONATOS : ",equipo_con_mas_goles)    
     
    
    f_equipo_recibiog(equipos)


#UNO DE LOS PUNTOS QUE ESCOGIMOS FUE REALIZAR EL MENU PRESENTADO A CONTINUACIÓN

#EJERCICIO 20
#REALIZAR MENU
#MENU 
salir = False
opcion = 0
 
while not salir:
    
    print("BIENVENIDO AL MENU DE FUTBOL")
    print ("1.Goles totales de los equipos locales")
    print ("2.Goles totales de los equipos visitantes")
    print ("3.Total de goles de todos los partidos")
    print ("4.Goles de equipos locales por campeonato")
    print ("5.Goles de equipos visitantes por campeonato")
    print ("6.Goles totales por campeonato")
    print ("7.Cantidad de partidos por equipo")
    print ("8.Selección que más goles anoto")
    print ("9.Selección que mas goles recibio")
    print ("10.Salir")
    print("Elija la opción que desea conocer:")
    opcion = int(input())
    
 
    if opcion == 1:
        print (ejercicio_1())
    elif opcion == 2:
        print (ejercicio_2())
    elif opcion == 3:
        print(ejercicio_3())
    elif opcion == 4:
        print (ejercicio_4())
    elif opcion == 5:
        print(ejercicio_5())
    elif opcion == 6:
        print(ejercicio_6())
    elif opcion == 7:
        print(ejercicio_7())
    elif opcion == 8:
        print(ejercicio_9())
    elif opcion == 9:
        print(ejercicio_10())
    elif opcion == 10:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 11")
 
print ("¡Fue placer servirte!")