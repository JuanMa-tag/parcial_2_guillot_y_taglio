from validaciones import validar_string_no_vacio
from mostrar_las_cartas import mostrar_cartas
def ordenar_cartas(lista_global):
    """
    (SORT)
    Permite ordenar la lista global por 'nombre' o 'elixir'.
    """
    print("\n--- 5. Ordenar Cartas ---")
    if not lista_global:
        print("No hay cartas para ordenar.")
        return

    print("Ordenar por:")
    print("  1. Nombre (A-Z)")
    print("  2. Elixir (Menor a Mayor)")
    opcion = validar_string_no_vacio("Opción: ")

    if opcion == '1':
        # 'key=lambda' define la función de ordenamiento
        lista_global.sort(key=lambda item: item['nombre'].lower())
        print("Lista ordenada por Nombre.")
    elif opcion == '2':
        lista_global.sort(key=lambda item: item['elixir'])
        print("Lista ordenada por Elixir.")
    else:
        print("Opción no válida.")
        
    # Mostramos los resultados del ordenamiento
    mostrar_cartas(lista_global)