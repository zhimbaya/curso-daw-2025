n = int(raw_input('Cuantos dias? '))

suma = 0.0
c_alzas = 0
mayores_que_490 = 0
mayor_alza = -float('inf')
mayor = -float('inf')

for i in range(n):
    actual = float(raw_input('Dia ' + str(i + 1) + ': '))
    suma += actual
    mayor = max(mayor, actual)

    if i != 0:   # el primer dia no hay precio anterior
        dif = actual - anterior
        if dif > 0:
            c_alzas += 1
            mayor_alza = max(mayor_alza, dif)

    if actual > 490:
        mayores_que_490 += 1

    # guardo el precio actual
    # para usarlo en la siguiente iteracion
    anterior = actual

print 'El promedio fue', int(10.0 * suma/n) / 10.0
print 'Hubo', mayores_que_490, 'precios mayores que 490'
if c_alzas > 0:
    print 'Hubo', c_alzas, 'alzas'
else:
    print 'No hubo alzas'
print 'El precio mayor fue', mayor
print 'La mayor de las alzas fue', mayor_alza
