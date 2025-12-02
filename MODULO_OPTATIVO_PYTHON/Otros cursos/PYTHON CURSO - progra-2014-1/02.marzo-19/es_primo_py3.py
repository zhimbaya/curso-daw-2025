# Entrada
n = int(input('n: ') or '50')

# Proceso
es_primo = n > 1
for d in range(2, n):
    if n % d == 0:
        es_primo = False
        break


# Salida
if es_primo:
    print ('Primo')
else:
    print ('No primo')


print(f"\nMostrar primos menores que: {n}")

# Verificamos que 'n' sea mayor que 2 para que haya primos que listar
if n > 2:
    # Bucle externo: Itera sobre todos los números desde 2 hasta n-1
    for numero in range(2, n):
        # 1. Asume que el número es primo
        es_primo_actual = True
        
        # 2. Bucle interno: Busca divisores desde 2 hasta el número-1
        # La forma más simple es ir hasta el número, sin optimizar por raíz cuadrada.
        for d in range(2, numero): 
            # Si encuentra un divisor, NO es primo
            if numero % d == 0:
                es_primo_actual = False
                break  # Detener la búsqueda de divisores (eficiente)

        # 3. Si sigue siendo True (es primo), imprimirlo
        if es_primo_actual:
            print(numero, end=' ')
            
    print() 
else:
    print("No hay números primos menores que el ingresado.")


