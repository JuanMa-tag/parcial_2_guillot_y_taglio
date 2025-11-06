import os
import csv
CARPETA_RAIZ = "ClashRoyale"
from validaciones import validar_entero_positivo, validar_string_no_vacio
def dar_de_alta_carta(carpeta_raiz):
    """
    (CREATE)
    Da de alta una nueva carta, creando la jerarquía de carpetas
    y escribiendo el archivo CSV en modo 'a' (append).
    """
    print("\n--- 1. Alta de Nueva Carta ---")
    
    # 1. ENTRADA DE DATOS (Jerarquía)
    print("Por favor, ingrese los 3 niveles de jerarquía:")
    rareza = validar_string_no_vacio("  -> Nivel 1 (Rareza): ").capitalize()
    tipo = validar_string_no_vacio("  -> Nivel 2 (Tipo): ").capitalize()
    alcance = validar_string_no_vacio("  -> Nivel 3 (Alcance): ").capitalize()

    # 2. ENTRADA DE DATOS (Atributos)
    print("\nAhora, ingrese los atributos de la carta:")
    nombre = validar_string_no_vacio("  -> Nombre de la carta: ")
    elixir = validar_entero_positivo(f"  -> Cantidad de Elixir para '{nombre}': ")
    
    # 4. CONSTRUCCIÓN DE RUTAS (Librería OS)
    ruta_directorio = os.path.join(carpeta_raiz, rareza, tipo, alcance)
    ruta_archivo_csv = os.path.join(ruta_directorio, 'datos.csv')
    
    print(f"\nPreparando para guardar en: {ruta_archivo_csv}")

    try:
        # 5. CREACIÓN DINÁMICA DE CARPETAS
        os.makedirs(ruta_directorio, exist_ok=True)
        
        # 6. PERSISTENCIA (Escritura en CSV)
        columnas = ['nombre', 'cantidad de elixir']
        nueva_carta = {'nombre': nombre, 'cantidad de elixir': elixir}
        
        es_archivo_nuevo = not os.path.isfile(ruta_archivo_csv)
        
        # Usamos modo 'a' (append) obligatorio
        with open(ruta_archivo_csv, mode='a', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=columnas)
            
            if es_archivo_nuevo:
                writer.writeheader() # Escribe encabezado si es nuevo
                
            writer.writerow(nueva_carta)
            
        print(f"\n¡ÉXITO! Carta '{nombre}' guardada correctamente.")
        return True # Devuelve True para indicar que hay que recargar
        
    except OSError as e:
        # 7. MANEJO DE EXCEPCIONES
        print(f"\nError de Sistema Operativo: No se pudo crear el directorio o escribir el archivo.")
        print(f"Detalle: {e}")
        return False
    except Exception as e:
        print(f"\nError inesperado durante la escritura del archivo: {e}")
        return False