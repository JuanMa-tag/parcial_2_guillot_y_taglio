def mostrar_cartas(lista_global):
    """
    (READ)
    Muestra una lista clara de todos los ítems registrados,
    incluyendo su jerarquía.
    """
    print("\n--- 2. Mostrar Ítems Totales ---")
    if not lista_global:
        print("No hay cartas cargadas en la lista.")
        return

    print(f"Mostrando un total de {len(lista_global)} cartas:")
    print("-" * 50)
    # Formateamos la salida para que sea legible
    print(f"{'Rareza':<12} | {'Tipo':<12} | {'Alcance':<10} | {'Nombre':<20} | {'Elixir':<6}")
    print("-" * 70)
    
    for carta in lista_global:
        print(f"{carta['rareza']:<12} | {carta['tipo']:<12} | {carta['alcance']:<10} | {carta['nombre']:<20} | {carta['elixir']:<6}")
    print("-" * 70)