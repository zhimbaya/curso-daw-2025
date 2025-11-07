mayor_puntaje = 0

while True:
    nombre = raw_input('Nombre: ')
    if nombre == 'FIN':
        break

    ######################################
    ## Preguntar el resto de los datos  ##
    ## y calcular el puntaje.           ##
    ######################################

    if puntaje > mayor_puntaje:
        mayor_puntaje = puntaje
        ganador = nombre

print 'El ganador es', ganador

