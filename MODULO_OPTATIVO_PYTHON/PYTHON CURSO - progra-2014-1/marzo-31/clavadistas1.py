mayor_puntaje = 0

nombre = raw_input('Nombre: ')
while nombre != 'FIN':

    ######################################
    ## Preguntar el resto de los datos  ##
    ## y calcular el puntaje.           ##
    ######################################

    if puntaje > mayor_puntaje:
        mayor_puntaje = puntaje
        ganador = nombre

    nombre = raw_input('Nombre: ')

print 'El ganador es', ganador

