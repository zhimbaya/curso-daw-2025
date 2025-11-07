archivo = open('notas.txt')

for linea in archivo:
    datos = linea.strip().split()
    nombre = datos[0]
    n1 = int(datos[2])
    n2 = int(datos[3])
    n3 = int(datos[4])

    promedio = (n1 + n2 + n3) / 3.0

    print 'El promedio de {0} es {1}'.format(nombre, promedio)

archivo.close()
