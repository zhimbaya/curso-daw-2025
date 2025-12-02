competencia = {
    'pista': {'v100mt', 'v400mt', 'v800mt', 'v3000mt', 'd100mt', 'd400mt'},
    'campo': {'vbala', 'vdisco', 'vslargo', 'dbala'},
}
puntaje = {
    'lugar 1': 12,
    'lugar 2':  9,
    'lugar 3':  7,
    'lugar 4':  5,
    'lugar 5':  4,
    'lugar 6':  3,
    'lugar 7':  2,
    'lugar 8':  1,
}
resultado = {
    'usm': [
        ('mrios',  'v400mt',   9),
        ('nmassu', 'v3000mt', 12),
        ('jrojas', 'vdisco',  12),
    ],
    'usach':[
        ('jramos', 'd400mt',   5),
        ('lsoto',  'd400mt',   9),
        ('mruiz',  'v800mt',   7),
    ],
    'uc':[
        ('mhard',  'v100mt',   3),
        ('msolis', 'd3000mt',  5),
        ('lrozas', 'dbala',    5),
    ]
}

def participante_prueba(competencia, resultado, prueba):
    participantes = []
    for u in resultado:
        deportistas = resultado[u]
        for d in deportistas:
            nombre, p, _ = d
            if p in competencia[prueba]:
                participantes.append(nombre)
    return participantes


def mayor_cantidad(resultado, puntaje):
    mayor = 0
    for u in resultado:
        deportistas = resultado[u]
        c = 0
        for d in deportistas:
            _, _, pts = d
            if pts == puntaje['lugar 1'] or pts == puntaje['lugar 2'] or pts == puntaje['lugar 3']:
                c += 1
        if mayor < c:
            mayor = c
            mejor_u = u
    return mejor_u


def prueba_sin_medallas(resultado,puntaje):
    con_medallas = []
    for u in resultado:
        deportistas = resultado[u]
        for nombre, prueba, pts in deportistas:
            if pts == puntaje['lugar 1'] or pts == puntaje['lugar 2'] or pts == puntaje['lugar 3']:
                con_medallas.append(prueba)

    sin_medallas = []
    for u in resultado:
        deportistas = resultado[u]
        for nombre, prueba, pts in deportistas:
            if prueba not in con_medallas:
                sin_medallas.append(prueba)
    return sin_medallas


print participante_prueba(competencia, resultado, 'campo')
print mayor_cantidad(resultado, puntaje)
print prueba_sin_medallas(resultado, puntaje)


