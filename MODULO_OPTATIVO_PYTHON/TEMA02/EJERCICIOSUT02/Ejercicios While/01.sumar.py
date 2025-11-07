'''
Escribe un programa que cuente hasta el número que desee el usuario. Nombre 
programa “sumar.py”.
'''
suma = 0

while True:
    try:
        print('-----Menú-----')
        print('1. Para sumar: ')
        print('5. Para salir: ')
        print('--------------')
        numero = int(input('Introduce una opción: '))
        if numero == 5:
            print('Hasta pronto!')
            break
        elif numero == 1:
            nsuma = int(input('Introduce el nº a sumar o "s" para salir '))
            
            while nsuma != 's':
                suma = suma + nsuma
                print('La suma total es: ', suma)
                nsuma = int(input('Introduce otro nº a sumar o "s" para salir: '))
        else:
            print('Opción incorrecta')
            numero = int(input('Vuelve a introducir una opción: '))
    except ValueError:
        print('Debe ingresar un valor entero')
        continue
    finally:
        print('Volviendo al menú principal')


