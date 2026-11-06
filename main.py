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

    if codigo <= 0 or nombre == '' or categoria == '' or precio < 0 or stock < 0:
        return False

    # Verificar que el código no exista
    indice, comparaciones = busqueda_secuencial(matriz, codigo)
    if indice != -1:
        return False

    matriz.append([codigo, nombre, categoria, precio, stock])
    return True


def baja_producto(matriz, codigo):
    # Elimina el producto. Devuelve True si lo eliminó, False si no existe.
    indice, comparaciones = busqueda_secuencial(matriz, codigo)
    if indice == -1:
        return False

    matriz.pop(indice)
    return True

def modificar_stock(matriz, codigo, cantidad):
    for i in range(len(matriz)):
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
    while fila_matriz < len(matriz) and codigo != matriz[fila_matriz][CODIGO_COLUMNA]:
        fila_matriz += 1
    if fila_matriz < len(matriz):
        return fila_matriz, (fila_matriz + 1)
    else:
        return -1, fila_matriz

def busqueda_binaria(matriz, codigo):
    # Requiere que la matriz esté ordenada por código (CODIGO_COLUMNA).
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
    # En cada pasada ubicamos el mayor restante en la posicion i (descendente).
    for i in range(len(matriz) - 1):
        pos_mayor = i

        for j in range(i + 1, len(matriz)):
            if matriz[j][columna] > matriz[pos_mayor][columna]:
                pos_mayor = j

        # Intercambiamos filas completas para conservar los datos del producto.
        auxiliar = matriz[i]
        matriz[i] = matriz[pos_mayor]
        matriz[pos_mayor] = auxiliar

    return matriz

def ordenar_insercion(matriz, columna):
    for i in range(1, len(matriz)):
        producto_actual = matriz[i]
        j = i - 1

        # Desplazamos hacia la derecha los productos con un valor menor (descendente).
        while j >= 0 and matriz[j][columna] < producto_actual[columna]:
            matriz[j + 1] = matriz[j]
            j -= 1

        # Colocamos el producto en el lugar que quedó libre.
        matriz[j + 1] = producto_actual

    return matriz

def ordenar_burbuja(matriz, columna):
    # Compara pares adyacentes y los intercambia si están en orden incorrecto (descendente).
    for i in range(len(matriz) - 1):
        for j in range(0, len(matriz) - 1 - i):
            if matriz[j][columna] < matriz[j + 1][columna]:
                auxiliar = matriz[j]
                matriz[j] = matriz[j + 1]
                matriz[j + 1] = auxiliar

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
    mas_caro = matriz[0]

    for i in range(1, len(matriz)):
        if matriz[i][PRECIO_COLUMNA] > mas_caro[PRECIO_COLUMNA]:
            mas_caro = matriz[i]

    return mas_caro


def producto_mas_barato(matriz):
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
    print("1)  Ver productos")
    print("2)  Agregar producto")
    print("3)  Baja de producto")
    print("4)  Modificar stock")
    print("5)  Búsqueda secuencial")
    print("6)  Búsqueda binaria (requiere orden por código)")
    print("7)  Ordenar por selección (mayor a menor)")
    print("8)  Ordenar por inserción (mayor a menor)")
    print("9)  Ordenar por burbuja (mayor a menor)")
    print("10) Reportes")
    print("11) Guardar CSV")
    print("12) Salir")

def pedir_columna():
    print("0) Código")
    print("1) Nombre")
    print("2) Categoría")
    print("3) Precio")
    print("4) Stock")
    columna = input("Elegí una columna: ")
    while not columna.isdigit() or int(columna) > STOCK_COLUMNA:
        columna = input("Ingresá un número entre 0 y 4: ")
    return int(columna)

def main():
    inventario = cargar_csv(ARCHIVO_CSV)
    seleccionMenu = ""
    while seleccionMenu != "12":
        listaMenu()
        seleccionMenu = entrada()

        if seleccionMenu == "1":
            print("\n--- Productos ---")
            for producto in inventario:
                print(producto)

        elif seleccionMenu == "2":
            print("\nAgregar producto:")
            codigo    = int(input("Código: "))
            nombre    = input("Nombre: ")
            categoria = input("Categoría: ")
            precio    = float(input("Precio: "))
            stock     = int(input("Stock: "))

            if alta_producto(inventario, codigo, nombre, categoria, precio, stock):
                print("Producto agregado.")
            else:
                print("No se pudo agregar. Código duplicado o datos inválidos.")

        elif seleccionMenu == "3":
            print("\nBaja de producto:")
            codigo = int(input("Código del producto a eliminar: "))

            if baja_producto(inventario, codigo):
                print("Producto eliminado.")
            else:
                print("Código no encontrado.")

        elif seleccionMenu == "4":
            print("\nModificar stock:")
            codigo   = int(input("Código del producto: "))
            cantidad = int(input("Cantidad a sumar o restar: "))

            if modificar_stock(inventario, codigo, cantidad):
                print("Stock modificado.")
            else:
                print("El código no existe o el stock quedaría negativo.")

        elif seleccionMenu == "5":
            print("\nBúsqueda secuencial:")
            codigo = int(input("Código a buscar: "))
            indice, comparaciones = busqueda_secuencial(inventario, codigo)

            if indice != -1:
                print("Producto encontrado:", inventario[indice])
                print("Comparaciones realizadas:", comparaciones)
            else:
                print("Producto no encontrado. Comparaciones realizadas:", comparaciones)

        elif seleccionMenu == "6":
            print("\nBúsqueda binaria (ordenando por código primero):")
            ordenar_seleccion(inventario, CODIGO_COLUMNA)
            codigo = int(input("Código a buscar: "))
            indice, comparaciones = busqueda_binaria(inventario, codigo)

            if indice != -1:
                print("Producto encontrado:", inventario[indice])
                print("Comparaciones realizadas:", comparaciones)
            else:
                print("Producto no encontrado. Comparaciones realizadas:", comparaciones)

        elif seleccionMenu == "7":
            print("\nOrdenar por selección (mayor a menor):")
            columna = pedir_columna()
            ordenar_seleccion(inventario, columna)
            for producto in inventario:
                print(producto)

        elif seleccionMenu == "8":
            print("\nOrdenar por inserción (mayor a menor):")
            columna = pedir_columna()
            ordenar_insercion(inventario, columna)
            for producto in inventario:
                print(producto)

        elif seleccionMenu == "9":
            print("\nOrdenar por burbuja (mayor a menor):")
            columna = pedir_columna()
            ordenar_burbuja(inventario, columna)
            for producto in inventario:
                print(producto)

        elif seleccionMenu == "10":
            print("\n--- Reportes ---")
            print("1) Productos con stock bajo umbral")
            print("2) Valor total del inventario")
            print("3) Producto más caro")
            print("4) Producto más barato")
            opcion = entrada()

            if opcion == "1":
                umbral = int(input("Umbral de stock: "))
                resultados = stock_bajo(inventario, umbral)
                if len(resultados) == 0:
                    print("No hay productos con stock bajo ese umbral.")
                else:
                    for p in resultados:
                        print(p)

            elif opcion == "2":
                print("Valor total del inventario: $", valor_total(inventario))

            elif opcion == "3":
                print("Producto más caro:", producto_mas_caro(inventario))

            elif opcion == "4":
                print("Producto más barato:", producto_mas_barato(inventario))

            else:
                print("Opción inválida.")

        elif seleccionMenu == "11":
            print("Guardando el CSV...")
            if guardar_csv(inventario, ARCHIVO_CSV):
                print("CSV guardado.")
            else:
                print("No se pudo guardar el CSV.")

        elif seleccionMenu == "12":
            print("Cerrando el programa...")

        else:
            print("Seleccioná una opción válida, intentá nuevamente.")

main()
