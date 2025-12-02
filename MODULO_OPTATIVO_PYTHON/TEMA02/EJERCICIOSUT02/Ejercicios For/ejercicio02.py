'''
EJERCICIO 2: Ejemplos prácticos del uso de range() en Python
Objetivo:
----------
Entender cómo funciona la función range() y aprender a generar secuencias
de números en diferentes situaciones usando sus distintas formas.
Instrucciones:
--------------
El programa mostrará ejemplos de las principales formas de usar range():
1️
⃣ range(fin)
- Genera números desde 0 hasta fin - 1.
2️
⃣ range(inicio, fin)
- Genera números desde 'inicio' hasta 'fin - 1'.
3️
⃣ range(inicio, fin, paso)
- Permite indicar un incremento o salto entre valores.
4️
⃣ range(inicio, fin, paso negativo)
- Cuenta hacia atrás cuando el paso es negativo.
5️
⃣ list(range(...))
- Convierte los objetos range en listas visibles para mostrar sus valores.
Aprendizaje:
-------------
Este ejercicio sirve para visualizar cómo range() crea secuencias de números
en distintos escenarios y cómo puede utilizarse en bucles for.
También se comprende que el valor final de range nunca se incluye.
'''


while True:
    print('''=====MENU=====
1️.range(fin) - Genera números desde 0 hasta fin - 1.
2️.range(inicio, fin) - Genera números desde 'inicio' hasta 'fin - 1'.
3️.range(inicio, fin, paso) - Permite indicar un incremento o salto entre valores.
4️.range(inicio, fin, paso negativo) - Cuenta hacia atrás cuando el paso es negativo.
5️.list(range(...)) - Convierte los objetos range en listas visibles para mostrar sus valores.
6. Salir
==========''')
    try:
        op = int(input('Selecciona una opción: '))
        if op == 6:
            print('Hasta pronto!')
            break
        elif op == 1:
            print('Genera números desde 0 hasta fin - 1')
            n = int(input('Introduce el nº limite: '))
            for i in range(n):
                print(i, end=' ')
            print('')
        elif op == 2:
            print("Genera números desde 'inicio' hasta 'fin - 1'.")
            x = int(input('Introduce el inicio: '))
            y = int(input('Introduce el fin: '))
            for i in range(x, y):
                print(i, end=' ')
            print('')
        elif op == 3:
            print("Permite indicar un incremento o salto entre valores.")
            x = int(input('Introduce el inicio: '))
            y = int(input('Introduce el fin: '))
            z = int(input('Introduce el incremento: '))
            for i in range(x, y, z):
                print(i, end=' ')
            print('')
        elif op == 4:
            print("Cuenta hacia atrás cuando el paso es negativo.")
            z = int(input('Introduce el decremento: '))
            for i in range(20, 4, z):
                print(i, end=' ')
            print('')
        elif op == 5:
            print(
                "Convierte los objetos range en listas visibles para mostrar sus valores.")
            print(list(range(4, 30, 3)))
        else:
            print('¡¡No es una opción válida!!')
    except Exception as e:
        print('Ha ocurrido un error', e)
