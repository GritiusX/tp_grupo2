ARCHIVO_CSV = 'inventario.csv'

def cargar_csv(nombre_archivo):
### open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    inventario = open(nombre_archivo, 'r', encoding='utf-8')
    lineas = inventario.readlines()
    print(lineas)
    return lineas

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


cargar_csv(ARCHIVO_CSV)