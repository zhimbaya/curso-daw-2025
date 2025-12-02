# Solucion que hicimos en clases.
# Resuelve el problema por separado para cada destino.

destino = raw_input('Destino: ')
autonomia = int(raw_input('Autonomia: '))
km = 0

if destino == 'B':
    while True:
        km += autonomia
        if km == 5:
            km -= 1

        if km < 16:
            print 'Acampa en km', km
        else:
            break

elif destino == 'C':
    while True:
        km += autonomia
        if km == 5 or km == 14:
            km -= 1

        if km < 21:
            print 'Acampa en km', km
        else:
            break


print 'Llega a', destino
