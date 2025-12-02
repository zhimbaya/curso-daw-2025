'''EJERCICIO 4: Contar múltiplos de 3 hasta un número dado por el usuario
Pedir al usuario un número límite y determinar cuántos múltiplos de 3 hay entre
1 y ese número. Además, mostrar por pantalla todos los múltiplos en una misma 
línea.
'''
n = int(input('Introduce el nº limite: '))

for i in range(n + 1):
    if i % 3 == 0:
        print(i, end=' ')
