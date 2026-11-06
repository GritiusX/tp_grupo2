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
    # Agrega un producto. Devuelve True si lo agregó,
    # False si el código ya existe o los datos no son válidos.

    # 1. Validar los datos... CAPAZ ACA HACER QUE SEA "not str" o algo asi xd
    if codigo <= 0 or nombre == '' or categoria == '' or precio < 0 or stock < 0:
        return False

    # 2. Verificar que el código no exista
    indice, comparaciones = busqueda_secuencial(matriz, codigo)
    if indice != -1:
        return False

    # 3. Agregar la fila con las columnas en el orden correcto
    matriz.append([codigo, nombre, categoria, precio, stock])
    return True


def baja_producto(matriz, codigo):
    # Elimina el producto. Devuelve True si lo eliminó, False si no existe.
    indice, comparaciones = busqueda_secuencial(matriz, codigo)
    if indice == -1:
        return False

    matriz.pop(indice)  # saca la fila que está en esa posición
    return True

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
    izquierda = 0
    derecha = len(matriz) - 1
    comparaciones = 0
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        if matriz[medio][CODIGO_COLUMNA] == codigo:
            return medio, comparaciones
        elif matriz[medio][CODIGO_COLUMNA] < codigo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1, comparaciones

def ordenar_seleccion(matriz, columna):
    # En cada pasada ubicamos el menor restante en la posicion i.
    for i in range(len(matriz) - 1):
        pos_menor = i

        for j in range(i + 1, len(matriz)):
            if matriz[j][columna] < matriz[pos_menor][columna]:
                pos_menor = j

        # Intercambiamos filas completas para conservar los datos del producto.
        auxiliar = matriz[i]
        matriz[i] = matriz[pos_menor]
        matriz[pos_menor] = auxiliar

    return matriz

def ordenar_insercion(matriz, columna):
    for i in range(1, len(matriz)):
        producto_actual = matriz[i]
        j = i - 1

        # Desplazamos hacia la derecha los productos con un valor mayor.
        while j >= 0 and matriz[j][columna] > producto_actual[columna]:
            matriz[j + 1] = matriz[j]
            j -= 1

        # Colocamos el producto en el lugar que quedó libre.
        matriz[j + 1] = producto_actual

    return matriz

def stock_bajo(matriz, umbral):
    resultados = []
    for i in range(len(matriz)):
        if matriz[i][STOCK_COLUMNA] < umbral:
            resultados.append(matriz[i])
    return resultados

def valor_total(matriz):
    total = 0
    for i in range(len(matriz)):
        total += matriz[i][PRECIO_COLUMNA] * matriz[i][STOCK_COLUMNA]
    return total

def producto_mas_caro(matriz):
    if len(matriz) == 0:
        return None
    mas_caro = matriz[0]
    for i in range(1, len(matriz)):
        if matriz[i][PRECIO_COLUMNA] > mas_caro[PRECIO_COLUMNA]:
            mas_caro = matriz[i]
    return mas_caro

def producto_mas_barato(matriz):
    if len(matriz) == 0:
        return None
    mas_barato = matriz[0]
    for i in range(1, len(matriz)):
        if matriz[i][PRECIO_COLUMNA] < mas_barato[PRECIO_COLUMNA]:
            mas_barato = matriz[i]
    return mas_barato

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
    print("5) Ordenar por selección (mayor a menor)")
    print("6) Ordenar por inserción (mayor a menor)")
    print("7) Salir")


def pedir_columna():
    # Pide al usuario por qué columna ordenar y devuelve su índice.
    print("Ordenar de menor a mayor por:")
    print("0) Código")
    print("1) Nombre")
    print("3) Precio")
    print("4) Stock")

    columna = input("Elegí una columna: ")
    while columna != "0" and columna != "1" and columna != "3" and columna != "4":
        columna = input("Ingresá 0, 1, 3 o 4: ")

    return int(columna)

def main():
    inventario = cargar_csv(ARCHIVO_CSV)
    seleccionMenu= ""
    while seleccionMenu != "7":
        listaMenu()
        seleccionMenu = entrada()

        if seleccionMenu == "1":
            print("Elegiste ver productos")
            for producto in inventario:
                print(producto)

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
            print("Ordenar de mayor a menor por:")
            print("0) Código")
            print("1) Nombre")
            print("2) Categoría")
            print("3) Precio")
            print("4) Stock")

            columna = input("Elegí una columna: ")

            while not columna.isdigit() or int(columna) > STOCK_COLUMNA:
                columna = input("Ingresá un número entre 0 y 4: ")

            ordenar_seleccion(inventario, int(columna))

            for producto in inventario:
                print(producto)
        elif seleccionMenu == "5":
            columna = pedir_columna()
            ordenar_seleccion(inventario, columna)

            for producto in inventario:
                print(producto)

        elif seleccionMenu == "6":
            columna = pedir_columna()
            ordenar_insercion(inventario, columna)

            for producto in inventario:
                print(producto)

        else: 
            print("Seleccioná una opción valida, intentá nuevamente")

main()
