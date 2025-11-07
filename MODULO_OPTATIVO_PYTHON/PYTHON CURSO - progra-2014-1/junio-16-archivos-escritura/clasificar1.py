def calcular_promedio(valores):
    n = float(len(valores))
    return sum(valores) / n

plantilla = '{0}:{1}:{2}\n'

# Abrir archivos
arch_curso = open('curso.txt')
arch_aprobados  = open('aprobados.txt',  'w')
arch_reprobados = open('reprobados.txt', 'w')

for linea in arch_curso:

    # Extraer informacion
    datos = linea.strip().split(':')
    nombre, apellido = datos[0:2]
    notas = map(float, datos[3:])
    promedio = int(round(calcular_promedio(notas)))

    # Escribir en el archivo correspondiente
    x = plantilla.format(nombre, apellido, promedio)
    if promedio < 55:
        arch_reprobados.write(x)
    else:
        arch_aprobados.write(x)

# Cerrar archivos
arch_curso.close()
arch_aprobados.close()
arch_reprobados.close()


