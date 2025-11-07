import os
from validaciones import validar_string_no_vacio
from reescribir_archivo import reescribir_archivo_csv
CARPETA_RAIZ = "ClashRoyale"
def eliminar_carta(lista_global, carpeta_raiz):
    """
    (DELETE)
    Busca una carta por nombre, la elimina de la memoria
    y luego sobrescribe el archivo CSV correspondiente.
    """
    print("\n--- 4. Eliminar Carta ---")
    if not lista_global:
        print("No hay cartas cargadas para eliminar.")
        return False

    nombre_buscar = validar_string_no_vacio("Ingrese el nombre exacto de la carta a eliminar: ")
    
    carta_encontrada = None
    try:
        for carta in lista_global:
            if carta['nombre'].lower() == nombre_buscar.lower():
                carta_encontrada = carta
                break
        
        if carta_encontrada:
            print(f"Carta encontrada: {carta_encontrada}")
            confirmacion = validar_string_no_vacio("¿Está seguro que desea eliminarla? (s/n): ").lower()
            
            if confirmacion == 's':
                # 1. Remover de la estructura en memoria
                lista_global.remove(carta_encontrada)
                
                # 2. Sobrescribir el archivo CSV
                print("Actualizando archivo...")
                
                cartas_del_mismo_archivo = [
                    c for c in lista_global
                    if c['rareza'] == carta_encontrada['rareza'] and
                        c['tipo'] == carta_encontrada['tipo'] and
                        c['alcance'] == carta_encontrada['alcance']
                ]
                
                ruta_directorio = os.path.join(carpeta_raiz, carta_encontrada['rareza'], carta_encontrada['tipo'], carta_encontrada['alcance'])
                ruta_archivo_csv = os.path.join(ruta_directorio, 'datos.csv')
                if reescribir_archivo_csv(ruta_archivo_csv, cartas_del_mismo_archivo):
                    print("¡ÉXITO! Carta eliminada y archivo actualizado.")
                    return True # Hay que recargar
            else:
                print("Eliminación cancelada.")
                return False
        else:
            raise ValueError(f"No se encontró ninguna carta con el nombre '{nombre_buscar}'.")
            
    except ValueError as e:
        # Manejo de excepción si no se encuentra
        print(f"Error: {e}")
        return False