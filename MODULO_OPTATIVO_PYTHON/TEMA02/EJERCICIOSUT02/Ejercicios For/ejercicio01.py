'''
EJERCICIO 1: Suma de los números del 1 al 5 con while y con for. Crea un 
programa que calcule la suma de los números del 1 al 5, 2 veces, la primera 
utilizando un bucle while y la segunda utilizando un bucle for, para comparar 
el funcionamiento de ambos tipos de bucles.
'''
#con for
suma= 0
for i in range(1,6):
    suma = suma + i
    print(suma)
print('Suma total con for = ',suma)


#con while
suma = 0
i=0
while i < 6:
    suma = suma + i
    print(suma)
    i+=1
print('Suma total con While = ',suma)