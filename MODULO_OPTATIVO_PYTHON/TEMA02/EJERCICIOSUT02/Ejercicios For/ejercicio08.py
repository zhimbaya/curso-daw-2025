'''
EJERCICIO 8: Determinar si un número es primo
Pedir al usuario un número entero positivo y comprobar si es un número primo.
Un número es primo si solo tiene dos divisores: 1 y él mismo.
Por ejemplo:
- 7 es primo → solo divisible por 1 y 7
- 12 no es primo → divisible por 1, 2, 3, 4, 6, 12
'''
n = int(input('Introduce un nº : ') or '12')

if n <= 0:
    print('No es un nº positivo')
elif n == 1:
    print('No es nº primo')
else:
    es_primo = True
    for i in range(2, n):
        if n % i == 0:
            print(f'Divisor de {n}: {i}')
            es_primo = False
            break  # ya encontramos un divisor, no es primo

    if es_primo:
        print('Es primo')
    else:
        print('No es primo')
