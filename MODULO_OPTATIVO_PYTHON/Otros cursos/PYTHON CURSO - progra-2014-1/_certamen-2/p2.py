vuelos = [
    # (vuelo, fecha_vuelo)
    (10, (2014,  1,  2)),
    (11, (2014,  1,  2)),
    (12, (2014,  1,  3)),
    (13, (2014,  5,  1)),
    (14, (2014,  5,  1)),
]

destinos = {
    10: {("Lima", "Peru"), ("San Jose", "Costa Rica"), ("Los Angeles", "USA")},
    11: {("San Jose", "Costa Rica"), ("Ciudad de Panama", "Panama")},
    12: {("Sao Paulo", "Brasil"), ("San Jose", "Costa Rica")},
    13: {("Lima", "Peru"), ("San Jose", "Costa Rica"), ("Ciudad de Panama", "Panama")},
    14: {("San Jose", "Costa Rica"), ("Buenos Aires", "Argentina")},
}

def vuelos_a_destino(destino, fecha):
    lista = []
    for vuelo in vuelos:
        nro_vuelo, fecha_vuelo = vuelo
        if fecha == fecha_vuelo:
            if destino in destinos[nro_vuelo]:
                lista.append(nro_vuelo)
    return lista


def destinos_repetidos():
    primero = True
    for nro in destinos:
        if primero:
            s = destinos[nro]
            primero = False
        else:
            s = s & destinos[nro]
    return s


def paises_visitados(fecha):
    s = set()
    for vuelo in vuelos:
        nro_vuelo, fecha_vuelo = vuelo
        if fecha == fecha_vuelo:
            for ciudad, pais in destinos[nro_vuelo]:
                s.add(pais)
    return s

print vuelos_a_destino(("San Jose", "Costa Rica"), (2014, 5, 1))
print destinos_repetidos()
print paises_visitados((2014, 5, 1))



