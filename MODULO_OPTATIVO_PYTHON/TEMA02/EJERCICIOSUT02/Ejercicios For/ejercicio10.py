'''
EJERCICIO 10:Pedir al usuario un número límite y calcular la suma de todos los 
números impares desde 1 hasta ese límite.
Los números pares se saltan usando la instrucción 'continue'.
'''
limite = int(input('Dame el límite: ') or '10')
suma = 0
for i in range(1, limite + 1):
    if i % 2 == 0:
        continue
    else:
        print(i)
        suma = suma + i
else:
    print('La suma de impares es: ', suma)
