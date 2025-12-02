# Esta es una version mejorada del programa
# que soporta abreviaciones con cantidades
# mayores que nueve, como por ejemplo:
#
#    12p4r1o11g00002r1a

abreviado = raw_input()

original = ''
veces = 0
for i in range(len(abreviado)):
    caracter = abreviado[i]
    if caracter in '0123456789':
        veces = 10 * veces + int(caracter)
    else:
        original += veces * caracter
        veces = 0

print original
