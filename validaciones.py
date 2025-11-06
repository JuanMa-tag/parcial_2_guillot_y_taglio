# --- 1. Funciones de Validación ---
def validar_string_no_vacio(prompt_mensaje):
    """
    Pide un dato al usuario y usa un bucle 'while' para asegurar
    que el dato no esté vacío.
    """
    while True:
        dato = input(prompt_mensaje).strip()
        if dato: # Si el string 'dato' NO está vacío
            return dato
        else:
            print("Error: Este campo no puede estar vacío. Intente de nuevo.")


def validar_entero_positivo(prompt_mensaje):
    """
    Pide un número al usuario y usa 'try-except' para asegurar
    que sea un entero positivo y mayor a cero.
    """
    while True:
        try:
            dato_str = input(prompt_mensaje).strip()
            dato_int = int(dato_str) # Intenta convertir a entero
            
            if dato_int > 0: # Valida lógica de negocio
                return dato_int
            else:
                print("Error: El número debe ser positivo y mayor a cero.")
                
        except ValueError:
            # ESTE ES EL USO DE TRY-EXCEPT PARA VALIDACIÓN
            print(f"Error: '{dato_str}' no es un número válido. Intente de nuevo.")