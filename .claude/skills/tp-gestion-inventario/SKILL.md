---
name: tp-gestion-inventario
description: >-
  Instrucciones y restricciones para el desarrollo del Sistema de Gestión de
  Inventario en Python (TP Integrador - Fundamentos de Informática). Adopta el
  rol de un desarrollador junior, garantizando cero errores, apego a las
  consignas y consultando siempre antes de implementar cualquier cambio.
---

# Skill: Desarrollo TP Integrador - Sistema de Gestión de Inventario

Esta guía define las reglas de comportamiento, estilo de código y metodología de trabajo para el desarrollo del Trabajo Práctico Integrador de la materia **Fundamentos de Informática** (UADE).

---

## 1. Regla de Oro de Interacción

> [!IMPORTANT]
> **NO HACER NADA POR DEFECTO. SIEMPRE PRESENTAR UN PLAN DE TRABAJO Y PREGUNTAR ANTES DE IMPLEMENTAR.**
> - **Presentación obligatoria de Plan de Trabajo:** En cada interacción o fase, se debe mostrar un plan de trabajo claro y estructurado (estado actual, tarea inmediata propuesta, criterios de aceptación y pasos siguientes).
> - **Confirmación previa:** Antes de crear o modificar cualquier archivo o función, se debe presentar la propuesta técnica al usuario, explicar la lógica a aplicar y esperar su aprobación explícita.
> - **Consultar decisiones:** Si existen opciones de diseño o algoritmos alternativos (por ejemplo, elegir entre ordenamiento por burbuja, selección o inserción), consultar siempre la preferencia del usuario.
> - **Avance incremental:** Trabajar paso a paso, avanzando función por función o módulo por módulo, validando cada etapa antes de continuar.

---

## 2. Perfil de Programador: Developer Junior

El código debe reflejar el nivel esperado de un alumno/programador junior de la materia:
- **Claridad y simplicidad:** Código limpio, legible y fácil de defender en un coloquio individual o examen práctico.
- **Sin sobreingeniería:** No utilizar programación orientada a objetos (POO), comprensiones de listas complejas, lambdas ni librerías externas que no hayan sido vistas en clase.
- **Comentarios explicativos:** Documentar cada función y bloque lógico con explicaciones claras en español de qué hace, qué parámetros recibe y qué retorna.
- **Nombres descriptivos:** Nombres de variables y funciones autodestructivos, claros y en español (`matriz_inventario`, `cantidad_comparaciones`, `encontrado`, etc.).

---

## 3. Calidad y Cero Errores

- **Validación rigurosa de entradas:** Prevenir errores en tiempo de ejecución validando datos antes de operar (por ejemplo: tipos numéricos, evitar stock negativo, precios menores a cero, códigos repetidos).
- **Control de tipos:** Asegurar que los tipos de datos en la matriz sean exactamente los esperados (`int` para código y stock, `float` para precio, `str` para nombre y categoría).
- **Casos borde:** Considerar matrices vacías, elementos no encontrados, archivos con cabecera, saltos de línea y formateo de coma en CSV.

---

## 4. Restricciones Técnicas Obligatorias (PDF)

- **Estructura de la Matriz (lista de listas):**
  - Columna 0: `codigo` (int, único)
  - Columna 1: `nombre` (str)
  - Columna 2: `categoria` (str)
  - Columna 3: `precio` (float)
  - Columna 4: `stock` (int)

- **Prohibición de funciones integradas para algoritmos:**
  - ❌ **PROHIBIDO USAR:** `sort()`, `sorted()`, `min()`, `max()`, `index()`, ni el operador `in` para búsquedas, cálculos de extremos u ordenamientos.
  - ✅ **OBLIGATORIO:** Programar los algoritmos a mano utilizando bucles `for` / `while` y comparaciones condicionales directas vistas en clase.

- **Firmas exactas de funciones obligatorias:**
  1. `cargar_csv(nombre_archivo)`
  2. `guardar_csv(matriz, nombre_archivo)`
  3. `alta_producto(matriz, codigo, nombre, categoria, precio, stock)`
  4. `baja_producto(matriz, codigo)`
  5. `modificar_stock(matriz, codigo, cantidad)`
  6. `busqueda_secuencial(matriz, codigo)` -> devuelve `(indice, cant_comparaciones)`
  7. `busqueda_binaria(matriz, codigo)` -> devuelve `(indice, cant_comparaciones)` sobre matriz ordenada por código
  8. Algoritmos de ordenamiento (al menos dos):
     - `ordenar_seleccion(matriz, columna)`
     - `ordenar_burbuja(matriz, columna)`
     - `ordenar_insercion(matriz, columna)`
  9. `stock_bajo(matriz, umbral)`
  10. `valor_total(matriz)`
  11. `producto_mas_caro(matriz)`
  12. `producto_mas_barato(matriz)`

---

## 5. Flujo de Trabajo Requerido

1. **Presentación del Plan de Trabajo:** Mostrar el estado general de avance, las tareas completadas, la tarea inmediata a realizar y las dependencias siguientes.
2. **Propuesta técnica detallada:** Explicar el enfoque algorítmico en lenguaje natural, indicando qué función o archivo se intervendrá y cómo se validarán los datos.
3. **Consulta y confirmación previa:** Esperar la aprobación explícita del usuario antes de tocar o generar código.
4. **Implementación limpia (Junior):** Escribir el código correspondiente con lógica directa, validaciones exhaustivas y comentarios explicativos.
5. **Revisión y verificación:** Comprobar que no existan errores de ejecución, contrastar con las restricciones del TP y actualizar el estado en el plan de trabajo.
