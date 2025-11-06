# parcial_2_guillot_y_taglio
parcial 2 de programacion 1pro4 prof hualpa
Integrantes: Tiago Nahuel Guillot Duran, Juan Manuel Carrillo Taglio

Este proyecto es un sistema de gestión de cartas (CRUD) para Clash Royale, desarrollado en Python como parte del Parcial 2 de Programación 1.

Su característica principal es que utiliza una estructura de carpetas jerárquica para persistir los datos, en lugar de un único archivo. El programa maneja la creación de estas carpetas y la lectura/escritura de los archivos CSV de forma dinámica.

 Diseño Técnico (Cómo se guardan los datos)
El sistema tiene un diseño de 3 niveles de jerarquía que mapea al sistema de archivos.

1. Jerarquía de Carpetas
La estructura de carpetas que genera el programa es:

Nivel 1 (Rareza): Comun, Especial, Epica, Legendaria

Nivel 2 (Tipo): Tropa, Estructura, Hechizo

Nivel 3 (Alcance): Terrestre, Aereo, Ambos

Por ejemplo, el "Pekka" se guardaría en la ruta: ClashRoyale/Epica/Tropa/Terrestre/datos.csv

2. Estructura del CSV
Cada archivo datos.csv solo contiene los atributos finales del ítem:

nombre,cantidad de elixir
Pekka,7
Principe,5
3. Lectura Recursiva
El programa utiliza una función recursiva (cargar_cartas) que explora el directorio raíz ClashRoyale/ y todos sus subdirectorios. Cuando encuentra un archivo datos.csv, lo lee y reconstruye el diccionario completo de la carta (incluyendo su rareza, tipo y alcance que obtiene de la ruta) en una única lista global en memoria.

## Requisitos
Python 3.x

.No se requieren librerías externas (solo os, csv y sys que vienen con Python).
.Asegúrate de tener Python 3 instalado en tu sistema.

## Instrucciones de Uso (Cómo ejecutar)

.El archivo (todas_las_cartas.csv) contiene todas las cartas del juego para usarlas de ejemplo ya
que estas no vienen incluidas en los otros archivos csv.

.Abre un terminal (CMD, PowerShell, o el terminal integrado de VS Code).

.Navega hasta la carpeta donde guardaste el archivo:

Bash

cd ruta/a/tu/carpeta
Ejecuta el script con Python:

Bash

python gestor_cartas.py

## Guía de Funcionalidades (Menú)
Al ejecutar el script, el programa te dará la bienvenida y mostrará el menú principal.

Arranque Inicial: La primera vez que lo ejecutes (antes de crear la carpeta ClashRoyale), te mostrará la advertencia: Advertencia: El directorio raíz 'ClashRoyale' no existe. y cargará 0 cartas. Esto es normal.

Opción 1: Alta de Nuevo Ítem (Crear)

Esta es la función principal para añadir datos.

Te pedirá los 3 niveles de jerarquía (Rareza, Tipo, Alcance).

Luego te pedirá los atributos (Nombre, Elixir).

Automáticamente, creará la estructura de carpetas (ej: ClashRoyale/Epica/Tropa/Terrestre/) si no existe, y añadirá la carta al archivo datos.csv correspondiente.

Opción 2: Mostrar Ítems Totales (Leer)

Muestra una tabla en la consola con todas las cartas encontradas por la función recursiva, indicando su jerarquía completa y atributos.

Opción 3 y 4: Modificación y Eliminación (Update/Delete)

Te pedirán el nombre exacto de la carta que deseas modificar o eliminar.

Buscarán la carta en la lista global cargada en memoria.

Una vez modificada o eliminada en memoria, el programa sobrescribirá (modo 'w') únicamente el archivo datos.csv específico donde esa carta estaba guardada, asegurando la persistencia del cambio.

Opción 5 y 6: Ordenamiento y Estadísticas

Estas funciones trabajan sobre la lista global de cartas.

Permiten ordenar la lista por Nombre o Elixir.

Muestran estadísticas clave como el conteo total, el promedio de elixir y un conteo de cartas por Rareza.

Opción 7: Recargar Datos desde Archivos

Vuelve a ejecutar la función recursiva (cargar_cartas) para limpiar la lista en memoria y volver a leer todos los archivos datos.csv.

Opción 8: Salir

Finaliza la ejecución del programa.