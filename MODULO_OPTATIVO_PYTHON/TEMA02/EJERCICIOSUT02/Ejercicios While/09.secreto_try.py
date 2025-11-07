'''
Escribir un programa que piense un número secreto y el usuario tenga que adivinarlo. 
De tal modo que:
El ordenador elige un número secreto entre 1 y 50. 
El jugador tiene 5 intentos para adivinarlo. 
En cada intento: 
● Si escribe 0, el juego termina y revela el número. 
● Si su número es menor, el programa dice “Demasiado bajo”. 
● Si es mayor, dice “Demasiado alto”. 
● Si acierta, se detiene con un mensaje de victoria. 
Si el jugador gasta los 5 intentos sin acertar, el programa revela el número secreto.
'''
import random
secreto = random.randint(1,50)
intentos = 5
contador = 0

while True:
    try:
        print('=====Adivina el número=====')
        print('0. para salir')
        print('1. adivinar')
        #print(secreto)
        print('='*30)
        opcion = int(input('Selecciona una opción: '))
        if opcion == 0:
            print('El número secreto era: ', secreto, 'Hasta pronto!')
            break
        elif opcion == 1:
            while contador < intentos:
                try: # se utiliza un try - except
                    numero = int(input('Introduce el número secreto: '))
                    if numero == secreto:
                        print('¡¡¡¡Has adivinado el número.!!!')
                        break
                    elif numero < secreto:
                        contador += 1
                        print('🔻 Número demasiado BAJO, intentos:',contador)
                    else:
                        contador +=1
                        print('🔺 Número demasiado ALTO, intentos: ', contador)
                except ValueError:
                    print('Introduce un número o digito')       
            if contador == intentos:
                print('El número secreto es: ', secreto ,', nº de intentos son:', contador)
                break
            
        else:
            print('Opción no valida!')
    except ValueError:
        print('Introduce un número, no una palabra')
        
    except Exception as e:
        print('Ocurrio un error: ', e)    