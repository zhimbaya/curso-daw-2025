def es_navidad(fecha):    # Solucion 1
    _, mes, dia = fecha
    if dia == 25 and mes == 12:
        return True
    else:
        return False

def es_navidad(fecha):    # Solucion 2
    _, mes, dia = fecha
    return dia == 25 and mes == 12

def es_navidad(fecha):    # Solucion 3
    _, mes, dia = fecha
    return (mes, dia) == (12, 25)


def nombre_completo(persona):
    nombre, apellido, _ = persona
    return nombre + ' ' + apellido

def edad(persona):
    _, _, fecha = persona
    a, _, _ = fecha
    return 2014 - a


def distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = x1 - x2
    dy = y1 - y2
    return (dx * dx + dy * dy) ** 0.5

def punto_medio(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    xm = (x1 + x2) / 2.0
    ym = (y1 + y2) / 2.0
    return (xm, ym)


def ganador(partido):
    equipos, resultado = partido

    local, visita = equipos
    gl, gv = resultado

    if gl > gv:
        return local
    elif gl < gv:
        return visita
    else:
        return 'Empate'

