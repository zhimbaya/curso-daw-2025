# Abrir archivos
arch_curso = open('curso.txt')
arch_aprobados  = open('aprobados.txt',  'w')
arch_reprobados = open('reprobados.txt', 'w')

for linea in arch_curso:

    # Extraer informacion
    datos = linea.strip().split(':')
    promedio = round(sum(map(int, datos[3:8])) / 5.0)

    # Escribir en el archivo correspondiente
    # (de una manera no muy elegante).
    if promedio < 55:
        arch_correspondiente = arch_reprobados
    else:
        arch_correspondiente = arch_aprobados
    arch_correspondiente.write(datos[0])
    arch_correspondiente.write(':')
    arch_correspondiente.write(datos[1])
    arch_correspondiente.write(':')
    arch_correspondiente.write(str(int(promedio)))
    arch_correspondiente.write('\n')

# Cerrar archivos
arch_curso.close()
arch_aprobados.close()
arch_reprobados.close()


