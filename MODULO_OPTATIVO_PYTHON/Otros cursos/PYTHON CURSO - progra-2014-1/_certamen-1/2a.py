anno_actual = int(raw_input('ingrese anio en curso: '))

while True:
    codigo = raw_input('ingrese un codigo: ')
    if codigo == 'fin':
        break
    anno = int(codigo[0] + codigo[1] + codigo[2] + codigo[3])
    ranking = int(codigo[7] + codigo[8] + codigo[9])
    antiguedad = anno_actual - anno

    if antiguedad == 2:
        descuento_antiguedad = 5
    elif antiguedad == 3:
        descuento_antiguedad = 15
    elif antiguedad >= 4:
        descuento_antiguedad = 25
    else:
        descuento_antiguedad = 0

    if ranking <= 10:
        descuento_ranking = 50
    elif 10 < ranking <= 20:
        descuento_ranking = 30
    elif 20 < ranking <= 30:
        descuento_ranking = 10
    else:
        descuento_ranking = 0

    descuento = max(descuento_antiguedad, descuento_ranking)
    print 'Al estudiante se le debe descontar un', descuento, '%'

