'''
Escribe un programa que adivine el número misterioso. El programa genera un número 
aleatorio entre 1 y 50. El jugador debe adivinarlo introduciendo números por teclado.
Después de cada intento, el programa indica si el número es demasiado alto o demasiado bajo.
Reglas: 
    ● Si el jugador introduce un número menor que 1 o mayor que 50, 
    el programa mostrará un aviso y NO contará ese intento. 
    ● Si el jugador escribe 0, se rinde y el programa termina. 
    ● El juego continúa hasta que el jugador adivina el número o se rinde.
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
            print('El número secreto era: ', secreto, ', Hasta pronto!')
            break
        elif opcion == 1:   
            
            while True:
                try:
                    numero = int(input('Introduce el número secreto o "0" para rendirte: '))
                    if numero == 0:
                        print('Me rindo!!!')
                        break
                    elif numero == secreto:
                        print('¡¡¡¡Has adivinado el número.!!!')
                        break
                    elif 0 < numero < secreto:
                        contador += 1
                        print('🔻 Número BAJO, intentos:',contador)
                    elif secreto < numero <= 50:
                        contador += 1
                        print('🔺 Número ALTO, intentos: ', contador)
                    elif numero < 0:
                        print('🔻 Número DEMASIADO BAJO, intentos:',contador)
                    elif numero > 50:
                        print('🔺 Número DEMASIADO ALTO, intentos: ', contador)
                    else:
                        pass
                except ValueError:
                    print('Dato invalido!')
        else:
            print('Opción no valida!')
    except ValueError:
        print('Introduce un número, no una palabra')
        
    except Exception as e:
        print('Ocurrio un error: ', e) 
    finally:
        print('='*40)