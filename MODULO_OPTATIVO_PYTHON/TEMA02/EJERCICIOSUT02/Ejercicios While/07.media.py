'''
Calcular la media de varios números hasta que el usuario escriba 0. .
Nombre programa “media.py”.
'''

print('-----Calcular la media-----')
contador = 0
suma = 0
media = 0

while True:
    try: 
        numero = int(input('Dime el número para la media o "0" para salir: '))
        if numero == 0:
            print('La media es: ', media)
            print('Hasta pronto!')
            break
        else:
            contador += 1
            suma = suma + numero
            media = suma/contador
            print('La suma total es: ', suma , contador)

    except ValueError:
        print('Valor introducido erroneo')
        
    except Exception as e:
        print('Ha ocurrido un error: ', e)
    