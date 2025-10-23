'''
Lógica booleana en una sola expresión
En este ejercicio vas a comprobar si un número cumple dos condiciones al mismo tiempo, usando operadores lógicos.
1. Pide al usuario un número entero.
2. Comprueba si está entre 1 y 100 (ambos incluidos).
3. Comprueba además si es múltiplo de 3 o de 5.
4. Muestra el resultado de esa comprobación en pantalla, 3 veces, usando imprimir normal con variables, 
imprimir con f-string simple e imprimir con f-string con operación.
'''
num_int = int(input("Dame un número entero: ") or "25")

num_entre = num_int >= 1 and num_int <= 100 # (1>= num_int <= 100)
num_mult = num_int % 3 == 0 or num_int % 5 == 0
es_valido = (num_entre) and (num_mult)

print("Comprobación: ", "Si" if es_valido else "No")
print(f"Comprboación: {es_valido}")
print(f"Comprobación: {(num_entre) and (num_mult)}")