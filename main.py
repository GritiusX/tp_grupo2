ARCHIVO_CSV = 'inventario.csv'
CODIGO_COLUMNA = 0 #index de la columna del codigo en el csv
NOMBRE_COLUMNA = 1 #index de la columna del nombre en el csv
CATEGORIA_COLUMNA = 2 #index de la columna de la categoria en el csv
PRECIO_COLUMNA = 3 #index de la columna del precio en el csv
STOCK_COLUMNA = 4 #index de la columna del stock en el csv

def cargar_csv(nombre_archivo):
    matriz = []

    ### open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    archivo = open(nombre_archivo, 'r', encoding='utf-8')
    lineas_archivo = archivo.readlines()
    archivo.close()

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
    # Guarda en una variable la matriz de productos del archivo CSV, con encabezado.
    archivo = open(nombre_archivo, 'w', encoding='utf-8')

    # Primera línea: encabezado
    archivo.write('codigo,nombre,categoria,precio,stock\n')

    # Una línea por producto (cada fila de la matriz)
    for fila in matriz:
        linea = (str(fila[CODIGO_COLUMNA]) + ',' + fila[NOMBRE_COLUMNA] + ',' + fila[CATEGORIA_COLUMNA] + ',' +
                 str(fila[PRECIO_COLUMNA]) + ',' + str(fila[STOCK_COLUMNA]) + '\n')
        archivo.write(linea)

    archivo.close()
    return True

def alta_producto(matriz, codigo, nombre, categoria, precio, stock):
    pass

def baja_producto(matriz, codigo):
    pass

def modificar_stock(matriz, codigo, cantidad):
    for i in range(len(matriz)):  # cargar_csv ya excluye el encabezado.
        producto = matriz[i]

        if producto[CODIGO_COLUMNA] == codigo:
            nuevo_stock = producto[STOCK_COLUMNA] + cantidad

            if nuevo_stock < 0:
                return False

            producto[STOCK_COLUMNA] = nuevo_stock
            return True
    
    return False
            

def busqueda_secuencial(matriz, codigo):
    fila_matriz = 0
    while fila_matriz < len(matriz) and codigo != matriz[fila_matriz][CODIGO_COLUMNA] :
        fila_matriz += 1
    if fila_matriz < len(matriz):
        return fila_matriz, (fila_matriz +1) ### fila_matriz +1 es el numero de comparaciones que se dio en la busqueda
    else:
        return -1 , fila_matriz

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
    print("3) Modificar stock")
    print("4) Guardar CSV")
    print("5) Salir")

def main():
    inventario = cargar_csv(ARCHIVO_CSV)
    seleccionMenu= ""
    while seleccionMenu != "5":
        listaMenu()
        seleccionMenu = entrada()

        if seleccionMenu == "1":
            print("Elegiste ver productos")

        elif seleccionMenu == "2":
            print("Elegiste agregar un producto")
        
        elif seleccionMenu == "3":
            print("Elegiste modificar el stock:")
            codigo = int(input("Código del producto: "))
            cantidad = int(input("Cantidad a sumar o restar: "))

            if modificar_stock(inventario, codigo, cantidad):
                print("Stock modificado")
            else:
                print("El codigo no existe o el stock quedaria negativo")

        elif seleccionMenu == "4":
            print("Guardando el CSV...")
            if guardar_csv(inventario, ARCHIVO_CSV):
                print("CSV guardado.")
            else:
                print("No se pudo guardar el CSV")

        elif seleccionMenu == "5":
            print("Cerrando el programa...")

        else: 
            print("Seleccioná una opción valida, intentá nuevamente")

main()


