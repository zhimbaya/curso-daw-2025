# Solucion usando operaciones aritmeticas.

depto = int(raw_input('Departamento: '))

piso = depto / 100
pos = depto % 100   # tambien podria ser: pos = depto - 100 * piso

base = 245
if depto == 807:
    print 500
elif piso == 1:
    print 100
elif piso == 25:
    print 400
# si llegamos a este punto, significa
# que ya estamos en un piso intermedio
elif pos == 0 or pos == 4:
    print int(base * (1.0 - 0.17))
elif pos == 3 or pos == 7:
    print int(base * (1.13))
else:
    print base

