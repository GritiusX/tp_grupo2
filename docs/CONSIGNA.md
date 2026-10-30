# TP Integrador - Sistema de Gestión de Inventario

Fundamentos de Informática - Comisión Viernes Noche - 2do Cuatrimestre 2026
FAIN / DEINI (UADE)

> Resumen de la consigna. El original está en [TP_Integrador_Consigna.pdf](TP_Integrador_Consigna.pdf).

## Fechas clave

| Instancia | Clase | Fecha | Detalle |
|---|---|---|---|
| Entrega de la consigna y armado de grupos | 9 | 02/10 | Grupos de 2 a 3 integrantes |
| Avance 1: matriz, menú, alta y carga desde CSV | 10 | 09/10 | Revisión en clase |
| Avance 2: búsqueda secuencial y binaria | 11 | 16/10 | Revisión en clase |
| Avance 3: métodos de ordenamiento | 12 | 23/10 | Revisión en clase |
| Consultas sobre el TP | 13 | 26/10 | Clase virtual sincrónica |
| Avance 4: baja, modificación, reportes y guardado | 14 | 30/10 | Pre-entrega: sistema completo funcionando |
| **Entrega final del TP** | — | **05/11** | Por el campus, hasta las 23:59 |
| Chequeo del TP con el docente | 15 | 06/11 | Aprobado / No aprobado |
| **Segundo Parcial** (individual, en computadora) | 16 | **13/11** | Basado en el TP |
| Reentrega (solo TP no aprobados) | 17 | 20/11 | Con las correcciones indicadas |
| **Coloquio final** (defensa individual) | 18 / 20 | **27/11 o 11/12** | Fecha por sorteo |

## Modalidad

- Grupos de 2 a 3 integrantes (individual solo con autorización del docente).
- Calificación Aprobado / No aprobado. Tener el TP aprobado es **condición para rendir el final**.
- El TP es grupal, pero el Segundo Parcial y el coloquio son **individuales**.
- Cada integrante tiene que poder explicar y modificar **todo** el código del grupo.

## Consigna

Desarrollar en Python un sistema de gestión de inventario para un pequeño comercio, que permita cargar, consultar, modificar y analizar el stock desde la consola.

### Estructura de datos (obligatoria)

Matriz (lista de listas), una fila por producto:

| Columna | Campo | Tipo | Ejemplo |
|---|---|---|---|
| 0 | Código (único) | `int` | `101` |
| 1 | Nombre | `str` | `"Yerba 1kg"` |
| 2 | Categoría | `str` | `"Almacén"` |
| 3 | Precio unitario | `float` | `3500.0` |
| 4 | Stock actual | `int` | `12` |

Archivo `inventario.csv` (con encabezado, separado por coma, mismo orden):

```
codigo,nombre,categoria,precio,stock
101,Yerba 1kg,Almacén,3500.0,12
102,Detergente 750ml,Limpieza,1800.0,4
```

### Funciones obligatorias (nombre y parámetros exactos)

| Función | Qué hace / qué devuelve |
|---|---|
| `cargar_csv(nombre_archivo)` | Lee el archivo y devuelve la matriz. |
| `guardar_csv(matriz, nombre_archivo)` | Escribe la matriz en el archivo, con encabezado. |
| `alta_producto(matriz, codigo, nombre, categoria, precio, stock)` | `True` si lo agregó; `False` si el código ya existe o los datos no son válidos. |
| `baja_producto(matriz, codigo)` | `True` si lo eliminó; `False` si no existe. |
| `modificar_stock(matriz, codigo, cantidad)` | Suma la cantidad (+/-) al stock. `False` si no existe o el stock quedaría negativo. |
| `busqueda_secuencial(matriz, codigo)` | Devuelve índice (o `-1`) y cantidad de comparaciones. |
| `busqueda_binaria(matriz, codigo)` | Igual, sobre la matriz ordenada por código. |
| `ordenar_seleccion(matriz, columna)`<br>`ordenar_burbuja(matriz, columna)`<br>`ordenar_insercion(matriz, columna)` | **Al menos dos** de las tres. Ordenan de menor a mayor por la columna y devuelven la matriz. |
| `stock_bajo(matriz, umbral)` | Lista de productos con stock menor al umbral. |
| `valor_total(matriz)` | Suma de precio × stock de todos los productos. |
| `producto_mas_caro(matriz)`<br>`producto_mas_barato(matriz)` | Devuelven la fila del producto. |

Se pueden agregar funciones auxiliares (mostrar matriz, pedir datos, etc.).

### Funcionalidades del programa

1. **Menú principal** que se repite hasta que el usuario sale.
2. **Carga inicial** de `inventario.csv` al iniciar.
3. **Alta, baja y modificación de stock**, validando datos.
4. **Búsqueda por código** con los dos métodos, informando las comparaciones de cada uno.
5. **Ordenamiento** por Nombre, Precio o Stock, a elección del usuario.
6. **Reportes**: listado ordenado; stock bajo (umbral ingresado); valor total; producto más caro y más barato.
7. **Guardar cambios** en `inventario.csv` antes de salir.

### Desafíos opcionales

- Interfaz gráfica con tkinter.
- Exportación adicional a JSON.
- Manejo de excepciones (`try/except`).

## Requisitos técnicos

- Cada operación es una **función con parámetros y valor de retorno**. Nada de lógica repetida suelta en el programa principal.
- Búsquedas, ordenamientos y máximo/mínimo **a mano**. Prohibido usar `sort()`, `sorted()`, `min()`, `max()`, `index()` y el operador `in` para resolverlos.
- Validar con condicionales lo que ingresa el usuario (ej.: precios o stock negativos).
- Nombres claros y código comentado.
- Usar solo herramientas vistas en la materia: cualquier otra cosa puede ser preguntada en el parcial y el coloquio.

## Uso de IA

- Se puede usar como apoyo (dudas, errores, revisión).
- Hay que **declarar en el informe** qué herramienta se usó y para qué.
- Todo el código tiene que poder ser explicado y modificado por cada integrante sin ayuda. Entregar código que no se puede explicar se considera falta de autoría.

## Entregables

Un integrante sube al campus, hasta el **05/11 a las 23:59**, un `TP_GrupoN.zip` con:

1. El código fuente (`.py`), comentado y funcionando.
2. `inventario.csv` con al menos **15 productos** de prueba.
3. Informe breve (máx. 3 páginas): integrantes; estructura de datos; descripción de las funciones principales; análisis de qué búsqueda y qué ordenamiento conviene y por qué; reparto del trabajo; declaración de uso de IA.

## Condiciones de aprobación (chequeo 06/11)

- [ ] El programa se ejecuta sin errores de principio a fin.
- [ ] Respeta la estructura de la matriz y los nombres/parámetros de las funciones obligatorias.
- [ ] Carga y guarda correctamente el CSV.
- [ ] Alta, baja y modificación de stock funcionan y validan datos.
- [ ] Búsqueda secuencial y binaria a mano, informando comparaciones.
- [ ] Al menos dos métodos de ordenamiento a mano.
- [ ] Los cuatro reportes funcionan.
- [ ] Uso correcto de funciones (parámetros y retorno), sin lógica repetida.
- [ ] Código comentado e informe completo.

Si no se aprueba: reentrega hasta el 20/11 (Clase 17).

## Evaluación a partir del TP

**Segundo Parcial — 13/11** (individual, en computadora, con grabación de pantalla):
- Un par de preguntas teóricas.
- Tres ejercicios **sin IA** sobre la matriz del inventario (solo bloc de notas o IDLE).
- Un ejercicio **con IA**.
- Se aprueba con 4. Recuperatorio: 27/11.

**Coloquio final — 27/11 o 11/12** (individual, por sorteo):
- Explicar partes del código y hacer **modificaciones en vivo, sin IA**.
- Requiere TP, Primer Parcial y Segundo Parcial aprobados.
