ARCHIVO_CSV = 'inventario.csv'

def cargar_csv(nombre_archivo):
### open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    inventario = open(nombre_archivo, 'r', encoding='utf-8')
    lineas = inventario.readlines()
    print(lineas)
    return lineas

def guardar_csv(matriz, nombre_archivo):
    pass

def alta_producto(matriz, codigo, nombre, categoria, precio, stock):
    pass

def baja_producto(matriz, codigo):
    pass

def modificar_stock(matriz, codigo, cantidad):
    for i in range(1, len(matriz)):  # Empieza en 1 para saltar los titulos.
        producto = matriz[i].strip().split(",")

        if int(producto[0]) == codigo:
            nuevo_stock = int(producto[4]) + cantidad

            if nuevo_stock < 0:
                return False

            producto[4] = str(nuevo_stock)
            matriz[i] = ",".join(producto) + "\n"
            return True
    
    return False
            

def busqueda_secuencial(matriz, codigo):
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
    print("3) Modificar stock")
    print("4) Salir")

def main():
    inventario = cargar_csv(ARCHIVO_CSV)
    seleccionMenu= ""
    while seleccionMenu != "4":
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
            print("Cerrando el programa...")

        else: 
            print("Seleccioná una opción valida, intentá nuevamente")

main()


