def calcular_promedio(valores):
    n = float(len(valores))
    return sum(valores) / n

plantilla = '{0:20} {1:>4} {2}\n'

# Abrir archivos
arch_curso = open('curso.txt')
arch_reporte  = open('promedios.txt', 'w')

# Escribir la cabecera de la tabla
cabecera = plantilla.format('Estudiante', 'Nota', 'Situacion')
raya = 35 * '-' + '\n'
arch_reporte.write(cabecera)
arch_reporte.write(raya)

for linea in arch_curso:

    # Extraer informacion
    datos = linea.strip().split(':')
    nombre, apellido = datos[0:2]
    notas = map(float, datos[3:])

    # Determinar datos a escribir
    nombre_completo = nombre + ' ' + apellido
    promedio = int(round(calcular_promedio(notas)))
    if promedio < 55:
        situacion = 'reprobado'
    else:
        situacion = 'aprobado'

    # Escribir la linea en el reporte
    x = plantilla.format(nombre_completo, promedio, situacion)
    arch_reporte.write(x)

# Cerrar archivos
arch_curso.close()
arch_reporte.close()


