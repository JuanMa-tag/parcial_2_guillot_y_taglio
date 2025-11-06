import os
from validaciones import validar_entero_positivo, validar_string_no_vacio
from reescribir_archivo import reescribir_archivo_csv
CARPETA_RAIZ = "ClashRoyale"
def modificar_carta(lista_global, carpeta_raiz):
    """
    (UPDATE)
    Busca una carta por nombre, permite modificarla en memoria
    y luego sobrescribe el archivo CSV correspondiente.
    """
    print("\n--- 3. Modificar Carta ---")
    if not lista_global:
        print("No hay cartas cargadas para modificar. Cargue los datos primero.")
        return False

    nombre_buscar = validar_string_no_vacio("Ingrese el nombre exacto de la carta a modificar: ")
    
    carta_encontrada = None
    for carta in lista_global:
        if carta['nombre'].lower() == nombre_buscar.lower():
            carta_encontrada = carta
            break
            
    if carta_encontrada:
        print(f"Carta encontrada: {carta_encontrada}")
        
        # 2. Solicitar qué modificar y el nuevo valor
        print("¿Qué atributo desea modificar?")
        print("  1. Nombre")
        print("  2. Cantidad de Elixir")
        opcion = validar_string_no_vacio("Opción: ")

        if opcion == '1':
            nuevo_nombre = validar_string_no_vacio("Nuevo nombre: ")
            carta_encontrada['nombre'] = nuevo_nombre
        elif opcion == '2':
            nuevo_elixir = validar_entero_positivo(f"Nuevo elixir para '{carta_encontrada['nombre']}': ")
            carta_encontrada['elixir'] = nuevo_elixir
        else:
            print("Opción no válida.")
            return False

        # 3. Sobrescribir el archivo CSV específico
        print("Actualizando archivo...")
        
        # Filtramos la lista global para obtener *solo* las cartas
        # que pertenecen al *mismo archivo* que la carta modificada.
        cartas_del_mismo_archivo = [
            c for c in lista_global
            if c['rareza'] == carta_encontrada['rareza'] and
               c['tipo'] == carta_encontrada['tipo'] and
               c['alcance'] == carta_encontrada['alcance']
        ]
        
        # Construimos la ruta del archivo a sobrescribir
        ruta_directorio = os.path.join(carpeta_raiz, carta_encontrada['rareza'], carta_encontrada['tipo'], carta_encontrada['alcance'])
        ruta_archivo_csv = os.path.join(ruta_directorio, 'datos.csv')
        
        # Llamamos a la función helper para reescribir
        if reescribir_archivo_csv(ruta_archivo_csv, cartas_del_mismo_archivo):
            print("¡ÉXITO! Carta modificada y archivo actualizado.")
            return True # Hay que recargar
    else:
        print(f"Error: No se encontró ninguna carta con el nombre '{nombre_buscar}'.")
        return False