'''
EJERCICIO 5: Calcular el factorial de un número
Pedir al usuario un número entero positivo y calcular su factorial.
El factorial de un número (n!) es el producto de todos los enteros positivos
desde 1 hasta n.
Por ejemplo:
5! = 1 × 2 × 3 × 4 × 5 = 120
'''
n = int(input('Introduce un nº para calcular su factorial: ') or '5')
factorial = 1
if n <= 0:
    print('No es un nº positivo')
else:
    
    for i in range(1, n + 1):
        factorial = factorial * i
        print(factorial,end=',')
    print(f'\nEl factorial de {n} es:',factorial)
