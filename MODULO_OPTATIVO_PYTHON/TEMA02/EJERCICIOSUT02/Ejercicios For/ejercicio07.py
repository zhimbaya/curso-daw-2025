'''
EJERCICIO 7: Números divisores de un número dado
Pedir al usuario un número entero positivo y mostrar todos los números
que son divisores exactos de ese número (es decir, que lo dividen sin dejar resto).
Por ejemplo:
Si el usuario introduce 12 → los divisores son 1, 2, 3, 4, 6 y 12.
'''
n = int(input('Introduce un nº : ') or '12')
if n <= 0:
    print('No es un nº positivo')
else:
    for i in range(1, n + 1):
        if n % i == 0:
            print(f'Divisor de {n}: ', i)
