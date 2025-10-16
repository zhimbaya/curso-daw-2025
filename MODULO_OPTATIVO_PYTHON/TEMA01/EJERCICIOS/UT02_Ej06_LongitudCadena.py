#Pedirá al usuario que introduzca un mensaje de texto.
mensaje = input('Introducir un mensaje de texto: ')

#Presentará en pantalla:
#El número de letras del texto
n_letras = len(list(mensaje))
print (f'El nº de letras son: {n_letras}')

#El número de palabras del texto
n_palabras = len(mensaje.split())
print (f'El nº de palabras son: {n_palabras}')

#Las palabras, separadas por comas
print(f'Mensaje separado por comas: {mensaje.replace(" ", ",")}')