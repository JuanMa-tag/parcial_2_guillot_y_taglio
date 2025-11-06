def mostrar_estadisticas(lista_global):
    """
    (STATS)
    Calcula y muestra estadísticas sobre el total de datos.
    """
    print("\n--- 6. Estadísticas Globales ---")
    if not lista_global:
        print("No hay datos para calcular estadísticas.")
        return

    # 1. Cantidad Total
    total_cartas = len(lista_global)
    print(f"Cantidad Total de Cartas: {total_cartas}")

    # 2. Promedio de Elixir
    try:
        suma_elixir = sum(carta['elixir'] for carta in lista_global)
        promedio_elixir = suma_elixir / total_cartas
        print(f"Costo Promedio de Elixir: {promedio_elixir:.2f}")
        
    except ZeroDivisionError:
        # Manejo de excepción si la lista está vacía (aunque ya lo chequeamos)
        print("Costo Promedio de Elixir: N/A")

    # 3. Recuento por categoría de primer nivel (Rareza)
    print("\nRecuento por Rareza (Nivel 1):")
    conteo_rareza = {}
    for carta in lista_global:
        rareza = carta['rareza']
        # .get(rareza, 0) obtiene el valor actual o 0 si no existe
        conteo_rareza[rareza] = conteo_rareza.get(rareza, 0) + 1
        
    for rareza, cantidad in conteo_rareza.items():
        print(f"  - {rareza}: {cantidad} cartas")