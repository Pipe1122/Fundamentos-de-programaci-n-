# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:56:24 2021

@author: Pipe
"""

# Lectura de archivos tipo Excel

import pandas as pd

# Leer el archivo de excel
df_archivoExcel = pd.read_excel('ventas_productos_1.xlsx', index_col='Producto')
df_archivoExcel = df_archivoExcel[ :10].copy()
print(df_archivoExcel)

# Grafica vertical
df_archivoExcel.plot(kind = 'bar')

# Grafica horizontal
df_archivoExcel.plot(kind = 'barh')

# Ocupar todo el espacio
df_archivoExcel.plot(kind = 'barh', width = 1) # Cada grupo de barras ocupa todo el espacio

# Grozor de las barras
df_archivoExcel.plot(kind = 'bar', 
                     stacked = 'True',)