from random import random

# random() retorna un real entre 0 y 1,
# pero no puede tomar el valor 1.
# Es decir, el valor retornado por random()
# siempre es "cero coma algo".
#
# Ver https://docs.python.org/2/library/random.html#random.random

def tirar_moneda():
    if random() < 0.5:
        return 'cara'
    return 'sello'


def tirar_cachipun():
    x = random()
    if x < 1.0/3.0:
        return 'tijera'
    elif x < 2.0/3.0:
        return 'papel'
    else:
        return 'piedra'


def tirar_dado():
    x = random() # x esta en el intervalo [0, 1[
    y = 6 * x    # y esta en el intervalo [0, 6[
    z = 1 + y    # z esta en el intervalo [1, 7[
    return int(z)


# Usaremos el pequen~o programita a continuacion
# para verificar que el dado no nos quedo desbalanceado.
# Lanzaremos el dado diez mil veces
# y esperaremos que los seis numeros aparezcan
# mas o menos la misma cantidad de veces.

# (El programa usa una lista,
# que es la materia que pasaremos dentro de poco)

c = [0, 0, 0, 0, 0, 0]
for i in range(10000):
    d = tirar_dado()
    c[d - 1] += 1
for d in range(1, 7):
    print 'El', d, 'salio', c[d - 1], 'veces'
