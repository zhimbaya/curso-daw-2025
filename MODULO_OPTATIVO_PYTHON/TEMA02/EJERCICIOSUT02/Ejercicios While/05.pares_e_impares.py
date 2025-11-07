'''
Mostrar los números pares hasta el número que diga el usuario y luego los 
impares hasta el número que el usuario diga.Nombre programa “pares_e_impares.py”.
'''
try:
    print('-----Calcular los pares e impares-----')
    print('1. pares')
    print('2. impares')
    print('3. salir')
    op = int(input('Selecciona una opción: '))
    while True:
        if op == 1:
            par = int(input('Dame un número para calcular sus pares: '))
            for i in range(par):
                if i%2 == 0:
                    print('El nº', i , "es par")
        elif op == 2:
            impar = int(input('Dame un número para calcular sus impares: '))
            for i in range(impar):
                if i%2 != 0:
                    print('El nº', i , "es Impar")
        elif op == 3:
            print("¡Hasta pronto!")
            break
        else:
            print('Opción incorrecta')
        
except ValueError:
    print('El valor introuducido no es el correcto')
except Exception as e:
    print('Ha ocurrido un error: ', e)