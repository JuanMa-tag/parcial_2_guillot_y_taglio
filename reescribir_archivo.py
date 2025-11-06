import os
import csv
def reescribir_archivo_csv(ruta_archivo, lista_cartas_archivo):
    """
    ( Update/Delete)
    Sobrescribe un archivo CSV específico con la lista de cartas
    proporcionada, usando el modo 'w' (write).
    """
    try:
        columnas = ['nombre', 'cantidad de elixir']
        
        # Abrimos en modo 'w' (write) para sobrescribir
        with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=columnas)
            writer.writeheader()
            
            for carta in lista_cartas_archivo:
                # Solo escribimos las columnas que van en el CSV
                writer.writerow({
                    'nombre': carta['nombre'],
                    'cantidad de elixir': carta['elixir']
                })
        return True
        
    except OSError as e:
        print(f"\nError de Sistema Operativo al sobrescribir {ruta_archivo}.")
        print(f"Detalle: {e}")
        return False
    except Exception as e:
        print(f"\nError inesperado al sobrescribir {ruta_archivo}: {e}")
        return False