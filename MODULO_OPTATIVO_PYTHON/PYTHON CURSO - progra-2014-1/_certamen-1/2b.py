anno_actual = int(raw_input('ingrese anio en curso: '))

codigo = raw_input('ingrese un codigo: ')
while codigo != 'fin':
    anno = int(codigo[0:4])
    ranking = int(codigo[7:10])
    antiguedad = anno_actual - anno

    # descuentos ordenados de mayor a menor
    if ranking <= 10:
        descuento = 50
    elif 10 < ranking <= 20:
        descuento = 30
    elif antiguedad >= 4:
        descuento = 25
    elif antiguedad == 3:
        descuento = 15
    elif 20 < ranking <= 30:
        descuento = 10
    elif antiguedad == 2:
        descuento = 5
    else:
        descuento = 0

    print 'Al estudiante se le debe descontar un', descuento, '%'

    codigo = raw_input('ingrese un codigo: ')


