def decodificar_palabra_stringona(abreviada):
    """
    Recibe una palabra abreviada (ej: '4p5r1o3g2r3a') y devuelve la palabra original 
    (ej: 'ppprrrrrogggrraaa').
    """
    palabra_original = ""
    i = 0  # Índice para recorrer la palabra abreviada

    # Recorrer la palabra abreviada de principio a fin
    while i < len(abreviada):
        # Paso 1: Leer el número de repeticiones
        
        # Asumimos que la primera posición (abreviada[i]) es el dígito 
        # que representa el número de repeticiones.
        # Lo convertimos a entero.
        try:
            num_repeticiones = int(abreviada[i])
        except ValueError:
            # Manejo de error si el formato es incorrecto, aunque el problema asume formato válido.
            print(f"Error: Carácter inesperado '{abreviada[i]}' encontrado en posición {i}. Se esperaba un número.")
            return "ERROR DE FORMATO"

        # Paso 2: Leer la letra a repetir
        
        # La letra siempre estará en la posición siguiente a la del número.
        if i + 1 < len(abreviada):
            letra = abreviada[i+1]
        else:
            # Si el número está al final de la cadena sin letra, es un error de formato.
            print(f"Error: Falta una letra después del número en la posición {i}.")
            return "ERROR DE FORMATO"
        
        # Paso 3: Construir el segmento de la palabra original
        
        # Añadir la letra repetida 'num_repeticiones' veces a la palabra original.
        # Multiplicar una cadena por un entero la repite (ej: 'p' * 4 = 'pppp').
        palabra_original += letra * num_repeticiones
        
        # Paso 4: Avanzar el índice
        
        # Nos movemos dos posiciones: una por el número y otra por la letra.
        i += 2
        
    return palabra_original

# --- Bloque principal del programa ---

# 1. Entrada de usuario
palabra_abreviada = input("Ingrese la palabra abreviada (Ej: 4p5r1o3g2r3a): ") or "4p5r1o3g2r3a"

# 2. Procesamiento
palabra_decodificada = decodificar_palabra_stringona(palabra_abreviada)

# 3. Salida
print("\n--- Resultado ---")
print(f"Palabra abreviada: {palabra_abreviada}")
print(f"Palabra original: {palabra_decodificada}")