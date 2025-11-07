# coding: utf-8

# Función auxiliar para convertir una linea del archivo
# en una tupla ((equipo, equipo), (goles, goles)).
def interpretar_partido(linea):
    partes = linea.strip().split('-')
    equipo_0, goles_0 = partes[0].split(';')
    equipo_1, goles_1 = partes[1].split(';')
    return ((equipo_0, equipo_1), (int(goles_0), int(goles_1)))


def obtener_equipos(nombre_archivo):
    equipos = set()
    archivo = open(nombre_archivo)
    for linea in archivo:
        (l, v), _ = interpretar_partido(linea)
        equipos.add(l)
        equipos.add(v)
    archivo.close()
    return list(equipos)


def obtener_clasificados(nombre_archivo):
    # A cada equipo vamos a asociar una tupla (puntos, diferencia_de_goles).
    # Aquí inicializaremos el diccionario.
    datos = {}
    for equipo in obtener_equipos(nombre_archivo):
        datos[equipo] = (0, 0)

    # Ahora vamos a calcular las estadísticas
    # después de que se jugaron los partidos.
    archivo = open(nombre_archivo)
    for linea in archivo:
        (l, v), (gl, gv) = interpretar_partido(linea)

        # Sacar del diccionario las estadísticas hasta el momento
        # para ambos equipos de este partido.
        pts_l, dif_l = datos[l]
        pts_v, dif_v = datos[v]

        # Actualizar los puntos.
        if gl > gv:    # Ganó l
            pts_l += 3
        elif gl < gv:  # Ganó v
            pts_v += 3
        else:          # Empate
            pts_l += 1
            pts_v += 1

        # Actualizar las diferencias de goles.
        dif_l += gl - gv
        dif_v += gv - gl

        # Guardar las estadísticas de vuelta en el diccionario.
        datos[l] = pts_l, dif_l
        datos[v] = pts_v, dif_v
    archivo.close()

    # A continuación llenaremos una lista de tuplas (pts, dif, equipo).
    # Al ordenarla, quedará primero ordenada por puntos y después por
    # diferencia de goles, que es justo lo que queremos.
    equipos = []
    for eq in datos:
        pts, dif = datos[eq]
        equipos.append((pts, dif, eq))
    equipos.sort()

    # La lista está ordenada de menor a mayor,
    # así que los equipos que nos interesan son los dos del final.
    _, _, primero = equipos[3]
    _, _, segundo = equipos[2]
    return (primero, segundo)


def partidos_octavos():
    archivo = open('Partidos_octavos.txt', 'w')
    plantilla = 'Grupo{}.txt'
    #for i, j in [(1, 2), (3, 4), (5, 6), (7, 8)]:
    for i, j in [(1, 2)]:
        primero_i, segundo_i = obtener_clasificados(plantilla.format(i))
        primero_j, segundo_j = obtener_clasificados(plantilla.format(j))
        archivo.write('{} v/s {}\n'.format(primero_i, segundo_j))
        archivo.write('{} v/s {}\n'.format(primero_j, segundo_i))
    archivo.close()

print obtener_equipos('Grupo2.txt')
print
print obtener_clasificados('Grupo2.txt')
print
partidos_octavos()
