import os
import csv
import sys
CARPETA_RAIZ = "ClashRoyale"
def cargar_cartas(ruta_actual, lista_total_cartas):
    """
    (READ)
    Función recursiva obligatoria. Recorre la jerarquía, lee los
    'datos.csv' y consolida todo en 'lista_total_cartas'.
    """
    try:
        elementos = os.listdir(ruta_actual)
    except FileNotFoundError:
        # Caso base para la primera llamada si la carpeta raíz no existe
        print(f"Advertencia: El directorio raíz '{CARPETA_RAIZ}' no existe. Se creará al añadir cartas.")
        return
    except OSError as e:
        print(f"Error al acceder a {ruta_actual}: {e}")
        return

    for elemento in elementos:
        ruta_completa_elemento = os.path.join(ruta_actual, elemento)

        if os.path.isdir(ruta_completa_elemento):
            # --- PASO RECURSIVO ---
            cargar_cartas(ruta_completa_elemento, lista_total_cartas)
        
        elif os.path.isfile(ruta_completa_elemento) and elemento == 'datos.csv':
            # --- CASO BASE ---
            
            # Extraemos la jerarquía desde la ruta
            try:
                ruta_carpeta = os.path.normpath(ruta_actual)
                partes_ruta = ruta_carpeta.split(os.sep)
                
                alcance = partes_ruta[-1]
                tipo = partes_ruta[-2]
                rareza = partes_ruta[-3]
                
            except IndexError:
                print(f"Advertencia: No se pudo extraer la jerarquía de {ruta_actual}. Omitiendo archivo.")
                continue 

            # --- Lectura Segura del Archivo ---
            try:
                with open(ruta_completa_elemento, mode='r', newline='', encoding='utf-8') as archivo_csv:
                    reader = csv.DictReader(archivo_csv)
                    
                    for fila in reader:
                        try:
                            carta_diccionario = {
                                'rareza': rareza.strip(),
                                'tipo': tipo.strip(),
                                'alcance': alcance.strip(),
                                'nombre': fila['nombre'].strip(),
                                'elixir': int(fila['cantidad de elixir'])
                            }
                            lista_total_cartas.append(carta_diccionario)
                            
                        except ValueError:
                            print(f"Error de formato en {ruta_completa_elemento}: El elixir '{fila['cantidad de elixir']}' no es un número.")
                        except KeyError:
                            print(f"Error de formato en {ruta_completa_elemento}: Falta la columna 'nombre' o 'cantidad de elixir'.")

            except FileNotFoundError:
                print(f"Error: El archivo {ruta_completa_elemento} no se encontró.")
            except Exception as e:
                print(f"Error inesperado al leer {ruta_completa_elemento}: {e}")