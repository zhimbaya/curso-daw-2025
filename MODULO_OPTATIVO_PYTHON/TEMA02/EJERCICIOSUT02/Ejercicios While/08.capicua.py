'''
Escribir un programa que te diga si un número es capicúa, 0 para salir. 
.Nombre programa “capicua.py”.
'''
print('-----Es capicua?-----')

while True:
    try: 
        numero = int(input('Dime el número o "0" para salir: '))
        if numero == 0:
            print('Hasta pronto!')
            break
        else:
            # se tiene que convertir en string
            n_capicua = str(numero)[::-1]
            if str(numero) == n_capicua:
                print(f'El numero {numero} es capicua')
            else:
                print('No es capicua')

    except ValueError:
        print('Valor introducido erroneo')
        
    except Exception as e:
        print('Ha ocurrido un error: ', e)