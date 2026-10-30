ARCHIVO_CSV = 'inventario.csv'
CODIGO_COLUMNA = 0 #index de la columna del codigo en el csv
NOMBRE_COLUMNA = 1 #index de la columna del nombre en el csv
CATEGORIA_COLUMNA = 2 #index de la columna de la categoria en el csv
PRECIO_COLUMNA = 3 #index de la columna del precio en el csv
STOCK_COLUMNA = 4 #index de la columna del stock en el csv

def cargar_csv(nombre_archivo):
    matriz = []
    ### range(start, stop, step)
    for fila in range(1,len(lineas_archivo)): ### fila es el indice de la fila en la matriz
        ### strip() elimina los espacios en blanco al principio y al final de la cadena
        columnas = lineas_archivo[fila].strip().split(',') 
        ### split(',') divide la cadena en una lista de subcadenas separadas por la coma
        columnas[CODIGO_COLUMNA] = int(columnas[CODIGO_COLUMNA])
        columnas[PRECIO_COLUMNA] = float(columnas[PRECIO_COLUMNA])
        columnas[STOCK_COLUMNA] = int(columnas[STOCK_COLUMNA])
        matriz.append(columnas) ### matriz.append(columnas) agrega la lista de columnas a la matriz

    #print(matriz)
    return matriz
  
def guardar_csv(matriz, nombre_archivo):
    # Escribe la matriz de productos en un archivo CSV, con encabezado.
    archivo = open(nombre_archivo, 'w', encoding='utf-8') # habria que normalizar aca y poner "inventario"?

    # Primera línea: encabezado
    archivo.write('codigo,nombre,categoria,precio,stock\n')

    # Una línea por producto (cada fila de la matriz)
    for fila in matriz:
        linea = (str(fila[0]) + ',' + fila[1] + ',' + fila[2] + ',' +
                 str(fila[3]) + ',' + str(fila[4]) + '\n')
        archivo.write(linea)

    archivo.close()

# ---- Prueba provisoria ----
# Matriz armada a mano (después va a venir de cargar_csv)
"""matriz_prueba = [
    [101, 'Yerba 1kg', 'Almacén', 3500.0, 12],
    [102, 'Detergente 750ml', 'Limpieza', 1800.0, 4]
]

guardar_csv(matriz_prueba, 'prueba.csv')   # guarda en un archivo aparte
cargar_csv('prueba.csv')      """       




#comment for pushing
=======
    ### open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    archivo = open(nombre_archivo, 'r', encoding='utf-8')
    lineas_archivo = archivo.readlines()
    archivo.close()


def alta_producto(matriz, codigo, nombre, categoria, precio, stock):
    pass

def baja_producto(matriz, codigo):
    pass

def modificar_stock(matriz, codigo, cantidad):
    pass

def busqueda_secuencial(matriz, codigo):
    fila_matriz = 0
    while fila_matriz < len(matriz) and codigo != matriz[fila_matriz][CODIGO_COLUMNA] :
        fila_matriz += 1
    pass

def busqueda_binaria(matriz, codigo):
    pass

def ordenar_seleccion(matriz, columna):
    pass

def ordenar_insercion(matriz, columna):
    pass

def stock_bajo(matriz, umbral):
    pass

def valor_total(matriz):
    pass

def producto_mas_caro(matriz): 
    pass

def producto_mas_barato(matriz): 
    pass

def entrada():
    seleccionMenu = input()
    while not seleccionMenu.isdigit():
        print("Porfavor seleccione un menú, solo con su número")
        seleccionMenu = input()
    return seleccionMenu


def listaMenu():
    print("\n---PANEL DE INVENTARIO---")
    print("1) Ver productos")
    print("2) Agregar productos")
    print("3) Salir")

def main():
    seleccionMenu= ""
    while seleccionMenu != "3":
        listaMenu()
        seleccionMenu = entrada()

        if seleccionMenu == "1":
            print("Elegiste ver productos")

        elif seleccionMenu == "2":
            print("Elegiste agregar un producto")
        
        elif seleccionMenu == "3":
            print("Cerrando el programa...")

        else: 
            print("Seleccioná una opción valida, intentá nuevamente")

#main()



cargar_csv(ARCHIVO_CSV)
