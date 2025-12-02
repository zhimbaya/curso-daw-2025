'''
EJERCICIO 6 — Calcular la suma de los cuadrados de los primeros N números
Suma de los cuadrados de los primeros N números
Pedir al usuario un número entero N y calcular la suma de los cuadrados
de todos los números desde 0 hasta N - 1.
Por ejemplo:
Si N = 5 → 0² + 1² + 2² + 3² + 4² = 30
'''
n = int(input('Introduce un nº para calcular sus cuadrados: ') or '5')
suma = 0
for i in range(n):
    suma = suma + i**2
    print(suma)
print('Suma total: ', suma)
