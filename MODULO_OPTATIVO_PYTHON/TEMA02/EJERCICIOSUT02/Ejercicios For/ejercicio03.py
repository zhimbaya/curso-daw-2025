'''
EJERCICIO 3 — Suma de números pares hasta un límite que indique el usuario.
Aquí nos damos cuenta de que, si ingresamos 8, nos suma 2+4+6, si quisieramos 
que llegara hasta el 8 deberíamos sumar 1, al limite o número que nos diga el 
usuario.
'''
n = int(input('Introduce el límite:'))
suma = 0
for i in range(0, n + 1, 2):
    suma = suma + i
    print(f'{i} = {suma}')
print('Suma total: ', suma)
