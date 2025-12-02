'''
EJERCICIO 9:Pedir al usuario un número límite y sumar los números naturales 
desde 1 en adelante hasta que la suma acumulada supere ese límite. En ese 
momento, el programa se detiene con 'break' y muestra el número que hizo que 
la suma sobrepasara el límite.
'''
limite = int(input('Dame el límite: ') or '15')
suma = 0
for i in range(1, limite):
    suma = suma + i
    print(suma)
    if suma > limite:
        break
    
print('La suma total es: ', suma)
