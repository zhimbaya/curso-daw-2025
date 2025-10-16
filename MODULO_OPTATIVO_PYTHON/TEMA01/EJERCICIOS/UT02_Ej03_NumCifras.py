#Preguntará al usuario un número entero
n_entero = int(input("Introduce un número entero: "))

#Se aplica las correspondientes funciones de conversión
n_digitos = len(list(str(abs(n_entero))))

#Presentará en pantalla:
#El número de dígitos del número
print(f'El número de dígitos del nº {n_entero} son: {n_digitos}')

