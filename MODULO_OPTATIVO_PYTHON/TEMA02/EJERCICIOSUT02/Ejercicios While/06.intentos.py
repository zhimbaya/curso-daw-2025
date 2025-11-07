'''
Contar cuántos intentos tarda el usuario en adivinar un número. .
Nombre programa “intentos.py”.
'''
import random

try:
    contador=0
    n_adivinar = random.randint(1, 20)
    while True:
        numero = int(input('Dime el número a adivinar: '))
        if numero == n_adivinar:
            print('Felicidades has adivinado el número: ', numero)
            break
        else:
            contador = contador + 1
            print(f'El número {numero}: no es el correcto,', 'nº de intentos = ',contador)
        
    print('Nº total de intentos = ', contador)
except ValueError:
    print('Valor introducido erroneo')
