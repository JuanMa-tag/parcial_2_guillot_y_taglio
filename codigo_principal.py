from Menu import mostrar_menu
from validaciones import validar_string_no_vacio
from Cargar_las_cartas import cargar_cartas
from Dar_de_alta_cartas import dar_de_alta_carta
from mostrar_las_cartas import mostrar_cartas
from modificar_las_cartas import modificar_carta
from Eliminar import eliminar_carta
from ordenar_las_cartas import ordenar_cartas
from Estadisticas import mostrar_estadisticas
CARPETA_RAIZ = "ClashRoyale"# Se define la carpeta raíz para todo el proyecto
def main():
    """Función principal que ejecuta el bucle del menú."""
    lista_global_de_cartas = []
    
    # Carga inicial de datos al arrancar
    print("Cargando datos iniciales...")
    cargar_cartas(CARPETA_RAIZ, lista_global_de_cartas)
    print(f"Carga inicial completa. {len(lista_global_de_cartas)} cartas cargadas.")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = validar_string_no_vacio("Seleccione una opción: ")
            
            if opcion == '1':
                # Crear 
                # Si el alta fue exitosa, recargamos la lista
                if dar_de_alta_carta(CARPETA_RAIZ):
                    print("Actualizando lista global...")
                    lista_global_de_cartas.clear() # Vaciamos
                    cargar_cartas(CARPETA_RAIZ, lista_global_de_cartas) # Recargamos
            
            elif opcion == '2':
                #Leer
                mostrar_cartas(lista_global_de_cartas)
                
            elif opcion == '3':
                #actuaizar
                # Si la modificación fue exitosa, no es necesario recargar
                # porque la lista en memoria ya fue actualizada.
                # (Aunque recargar también sería válido y más seguro)
                modificar_carta(lista_global_de_cartas, CARPETA_RAIZ)

            elif opcion == '4':
                #Eliminar
                # Si la eliminación fue exitosa, no es necesario recargar
                # porque la lista en memoria ya fue actualizada.
                eliminar_carta(lista_global_de_cartas, CARPETA_RAIZ)

            elif opcion == '5':
                #ordenamiento
                ordenar_cartas(lista_global_de_cartas)
                
            elif opcion == '6':
                #estadisticas 
                mostrar_estadisticas(lista_global_de_cartas)

            elif opcion == '7':
                # RECARGA MANUAL
                print("Recargando todos los datos desde los archivos...")
                lista_global_de_cartas.clear()
                cargar_cartas(CARPETA_RAIZ, lista_global_de_cartas)
                print(f"¡Datos recargados! {len(lista_global_de_cartas)} cartas en memoria.")
                
            elif opcion == '8':
                print("¡Hasta luego!")
                break # Rompe el bucle while True
                
            else:
                print("Error: Opción no válida. Intente de nuevo.")
                
        except Exception as e:
            # Captura de emergencia para cualquier error no esperado
            print(f"Ha ocurrido un error inesperado en el menú: {e}")


# Punto de Entrada Principal
if __name__ == "__main__":
    main()