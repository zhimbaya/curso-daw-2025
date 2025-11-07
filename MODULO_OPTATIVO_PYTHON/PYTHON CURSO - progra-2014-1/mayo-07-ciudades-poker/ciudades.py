# Las dos primeras funciones deben retornar un conjunto.
# Cuando este es el caso, generalmente hay que comenzar
# creando un conjunto vacio, luego llenarlo y finalmente retornarlo:
#
#    def funcion(parametros):
#        conjunto = set()
#        for ... in ...:
#            conjunto.add(algo)
#        return conjunto
#

# Solucion 1: crear un conjunto vacio
# y agregar las llaves una por una.
def ciudades(info):
    cs = set()
    for ciudad in info:
        cs.add(ciudad)
    return cs

# Solucion 2: al convertir un diccionario a conjunto
# se obtienen las llaves.
def ciudades2(informacion):
    return set(informacion)


# Solucion 1: igual que arriba, solo que hay
# que obtener la region a partir de la llave.
def regiones(info):
    rs = set()
    for ciudad in info:
        region, anno = info[ciudad]
        rs.add(region)
    return rs

# Solucion 2: iterar directamente sobre los valores.
# A mi esta forma no me gusta porque es algo mas que hay que aprender
# a pesar de que siempre se puede hacer iterando sobre las llaves.
def regiones2(info):
    rs = set()
    for valor in info.values():
        region, _ = valor
        rs.add(region)
    return rs


# La funcion ciudades_por_region debe retornar un diccionario
# cuyas llaves son conjuntos. Analogamente a lo que hicimos arriba,
# hay que crear un diccionario vacio, llenarlo y retornarlo:
#
#    def funcion(parametros):
#        d = {}
#        ...
#        return d
#
# Inicialmente, no existen los conjuntos a los que hay que agregar las
# ciudades. Por lo tanto, para cada ciudad hay que tener la precaucion de
# crear el conjunto para su region cuando este no existe aun.

# Solucion 1: recorrer las ciudades una por una.
# Si la region no esta aun en el diccionario,
# se inicializa su conjunto. A continuacion, se agrega
# la ciudad al conjunto asociado a la region.
def ciudades_por_region(info):
    cpr = {}
    for ciudad in info:
        region, _ = info[ciudad]
        if region not in cpr:    # creamos el conjunto si no existe aun
            cpr[region] = set()
        cpr[region].add(ciudad)  # agregamos la ciudad al conjunto
    return cpr

# Solucion 2: primero inicializar los conjuntos para todas las regiones.
def ciudades_por_region2(info):
    cpr = {}
    for region in regiones(info):
        cpr[region] = set()

    # Ahora cada region ya tiene su conjunto creado. Solo falta llenarlos.
    for ciudad in info:
        region, _ = info[ciudad]
        cpr[region].add(ciudad)

    return cpr

# Solucion 3: usar el metodo .items() para obtener la llave y el valor a la vez.
# Nuevamente, a mi no me gusta esta forma. Siempre prefiero iterar sobre las llaves.
def ciudades_por_region3(info):
    cpr = {}
    for ciudad, (region, _) in info.items():

        # Una pequen~a variacion: en vez de crear el diccionario vacio
        # y despues agregar la ciudad, cuando la llave no existe le asocio
        # inmediatamente el conjunto con la ciudad.
        if region not in cpr:
            cpr[region] = {ciudad}
        else:
            cpr[region].add(ciudad)

    return cpr


if __name__ == '__main__':
    info = {
      'Arica':        ('XV',   1570),
      'Concepcion':   ('VIII', 1550),
      'Osorno':       ('X',    1558),
      'Puerto Montt': ('X',    1853),
      'Chillan':      ('VIII', 1580)
    }
    # Si las funciones no entregan el resultado correcto,
    # el programa se va a caer en alguna de estas aserciones.
    assert ciudades(info)  == {'Concepcion', 'Osorno', 'Arica', 'Chillan', 'Puerto Montt'}
    assert ciudades2(info) == {'Concepcion', 'Osorno', 'Arica', 'Chillan', 'Puerto Montt'}
    assert regiones(info)  == {'X', 'XV', 'VIII'}
    assert regiones2(info) == {'X', 'XV', 'VIII'}
    assert ciudades_por_region(info)  == {'X': {'Puerto Montt', 'Osorno'}, 'VIII': {'Concepcion', 'Chillan'}, 'XV': {'Arica'}}
    assert ciudades_por_region2(info) == {'X': {'Puerto Montt', 'Osorno'}, 'VIII': {'Concepcion', 'Chillan'}, 'XV': {'Arica'}}
    assert ciudades_por_region3(info) == {'X': {'Puerto Montt', 'Osorno'}, 'VIII': {'Concepcion', 'Chillan'}, 'XV': {'Arica'}}

