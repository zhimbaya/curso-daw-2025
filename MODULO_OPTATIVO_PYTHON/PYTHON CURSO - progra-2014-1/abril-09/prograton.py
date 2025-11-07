total = 0
mayor = 0
cuenta = 1
while total < 20000:
    donacion = int(raw_input('Donacion: '))
    total += donacion
    if donacion > mayor:
        mayor = donacion
        mejor_donante = cuenta
    cuenta += 1
print 'Se logro la meta!'
print 'Gracias al donante', mejor_donante, 'por aportar', mayor


