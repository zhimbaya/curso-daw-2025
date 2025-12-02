ganados_a = 0
ganados_b = 0
while ganados_a < 3 and ganados_b < 3:
    a = raw_input('A: ')
    b = raw_input('B: ')

    ###########################
    ## Determinar al ganador ##
    ## de la partida.        ##
    ###########################

    if ganador == 'A':
        ganados_a += 1
    elif ganador == 'B':
        ganados_b += 1
    print ganados_a, '-', ganados_b

if ganados_a > ganados_b:
    print 'La ganadora es A'
else:
    print 'El ganador es B'

