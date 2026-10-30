ARCHIVO_CSV = 'inventario.csv'

def cargar_csv(nombre_archivo):
### open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    inventario = open(nombre_archivo, 'r', encoding='utf-8')
    lineas = inventario.readlines()
    print(lineas)
    return lineas

#def guardar_csv(matriz, nombre_archivo)



cargar_csv(ARCHIVO_CSV)