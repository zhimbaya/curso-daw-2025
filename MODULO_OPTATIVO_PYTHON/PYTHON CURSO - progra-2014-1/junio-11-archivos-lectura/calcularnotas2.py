def promedio(notas):
    return round(float(sum(notas)) / len(notas))


archivo = open('notas.txt')

for linea in archivo:
    datos = linea.strip().split()
    nombre = datos[0]
    notas = map(int, datos[2:5])
    p = promedio(notas)
    print 'El promedio de {0} es {1}'.format(nombre, p)

archivo.close()
