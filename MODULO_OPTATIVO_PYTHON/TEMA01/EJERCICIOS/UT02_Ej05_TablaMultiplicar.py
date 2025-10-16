#Preguntará al usuario un número entre 0 y 9
numero0_9=int(input('Introducir un numero entre 0 y 9: '))

#Presentará en pantalla:
#Tabla de multiplicar del número (multiplicando por los números del 1 al 10)
print('=' * 25)
print(f'Tabla de multiplar del nº {numero0_9}')
print('--------------------------------------')
print(f"{numero0_9} x 1 = {numero0_9 * 1}")
print(f"{numero0_9} x 2 = {numero0_9 * 2}")
print(f"{numero0_9} x 3 = {numero0_9 * 3}")
print(f"{numero0_9} x 4 = {numero0_9 * 4}")
print(f"{numero0_9} x 5 = {numero0_9 * 5}")
print(f"{numero0_9} x 6 = {numero0_9 * 6}")
print(f"{numero0_9} x 7 = {numero0_9 * 7}")
print(f"{numero0_9} x 8 = {numero0_9 * 8}")
print(f"{numero0_9} x 9 = {numero0_9 * 9}")
print(f"{numero0_9} x 10 = {numero0_9 * 10}")

#Marcos de separación representados por caracteres (por ejemplo "=====")
print('=' * 25)

#Mensaje de despedida
print('Hasta pronto!')
