archivo = open('notas.txt')

for linea in archivo:
    datos = linea.strip().split(',')
    nombre = datos[0]
    fecha = map(int, datos[1].split('/'))
    a, _, _ = fecha
    edad = 2014 - a

    print 'La edad de {0} es {1}'.format(nombre, edad)

archivo.close()
