# Factura de venta

def f_titulo():
    print("Calculo valor Factura")
    
def f_despedida():
    print("...Adios...")    

def f_valorfactura(): # Encabezado de la función
    # Desarrollo de la función
    
    # Variables
    ve_nom_art = ""
    ve_cant_art = 0
    ve_valor_unid_art = 0.0
    
    cons_por_iva = 0.19
    
    vps_neto = 0.0
    vps_iva = 0.0
    vps_total = 0.0
    
    # Entradas
    ve_nom_art = input("Articulo:")
    ve_cant_art = int (input("Cantidad:"))
    ve_valor_unid_art = float (input("Valor unitario:"))
    
    # Procesos
    vps_neto = ve_cant_art * ve_valor_unid_art
    vps_iva = vps_neto * cons_por_iva
    vps_total = vps_neto + vps_iva
    
    # Salidas
    print("Neto", vps_neto)
    print("IVA", vps_iva)
    print("Total", vps_total)
    
# Llamado de la funcion
f_titulo()
f_valorfactura()
f_despedida()

