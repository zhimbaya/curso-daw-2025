# Abrir archivos
arch_curso = open('curso.txt')
arch_aprobados  = open('aprobados.txt',  'w')
arch_reprobados = open('reprobados.txt', 'w')

for linea in arch_curso:

    # Extraer informacion
    datos = linea.strip().split(':')
    nombre = datos[0]
    apellido = datos[1]
    # Ojo: esto sirve solo si son exactamente cinco notas
    n1, n2, n3, n4, n5 = map(float, datos[3:8])
    promedio = int(round((n1 + n2 + n3 + n4 + n5) / 5.0))

    # Escribir en el archivo correspondiente
    x = ':'.join([nombre, apellido, str(promedio)]) + '\n'
    if promedio < 55:
        arch_reprobados.write(x)
    else:
        arch_aprobados.write(x)

# Cerrar archivos
arch_curso.close()
arch_aprobados.close()
arch_reprobados.close()


