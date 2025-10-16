#Preguntará el nombre y la edad a 3 personas
nombre1 = input('Introduce tu nombre: ')
edad1 = int(input('Introduce tu edad: '))
nombre2 = input('Introduce tu nombre: ')
edad2 = int(input('Introduce tu edad: '))
nombre3 = input('Introduce tu nombre: ')
edad3 = int(input('Introduce tu edad: '))

#Presentará en pantalla:
#Nombre y la edad de cada uno.
print('---------------------')
print(f'Nombre 1: {nombre1}')
print (f'Edad 1: {edad1}')
print(f'Nombre 2: {nombre2}')
print (f'Edad 2: {edad2}')
print(f'Nombre 3: {nombre3}')
print (f'Edad 3: {edad3}')
print('---------------------')

#Edad media de todas las personas.
edad_media = (edad1 + edad2 + edad3)/3
print(f'La edad media de todas las personas es: {edad_media:.2f} años')
