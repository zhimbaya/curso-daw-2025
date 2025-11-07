'''
Escriba un programa que cuente los números del 1 hasta el que desee el usuario. 
Por ejemplo, si nos dice 3, tendríamos que contar 1+2+3=6. Nombre programa “contar.py”.
'''
#menu
print('-----Menú-----')
print('1. Para sumar: ')
print('5. Para salir: ')
print('--------------')

suma = 0

while True:
    try:
        numero = int(input('Introduce una opción: '))
        if numero == 5:
            print('Hasta pronto!')
            break
        elif numero == 1:
            nsuma = int(input('Introduce el nº a sumar: '))
            for i in range(1, nsuma + 1):
                suma = suma + i
                print(f'Nº {i}, la suma = {suma}')
            print('La suma total es: ', suma)
        else:
            print('Opción incorrecta')
            numero = int(input('Vuelve a introducir una opción: '))
    except ValueError:
        print('Debe ingresar un valor entero')
        continue
    finally:
        print('Volviendo al menú principal')
'''
suma = 0
for i in range(1,numero+1):
    suma = suma + i
    print('Número: ',i)
    
print('La suma total es: ', suma)
'''
'''
suma = 0
i = 1
while i <= numero:
    suma = suma + i
    print('Número: ',i)
    i+=1
    
print('La suma total es: ', suma)
'''