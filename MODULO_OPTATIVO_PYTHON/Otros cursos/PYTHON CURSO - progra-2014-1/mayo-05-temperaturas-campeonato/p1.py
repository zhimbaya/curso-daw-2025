def llaves(diccionario):
    ls = []
    for llave in diccionario:
        ls.append(llave)
    return ls


# Otra solucion:
def llaves(diccionario):
    # Al convertir un diccionario a lista,
    # se obtiene una lista de las llaves.
    return list(diccionario)


# Esta funcion es casi igual a llaves,
# solo que hay que obtener el valor a partir de cada llave
# para poder agregarlo a la lista.
def valores(diccionario):
    vs = []
    for llave in diccionario:
        valor = diccionario[llave]
        vs.append(valor)
    return vs


# La funcion invertir debe retornar un nuevo diccionario,
# y no modificar el que recibe como parametro.
def invertir(diccionario):
    invertido = {}
    for llave in diccionario:
        valor = diccionario[llave]
        invertido[valor] = llave
    return invertido


def unir(da, db):
    unido = {}

    # Recorremos ambos diccionarios por separado
    # y vamos copiando sus valores al nuevo diccionario.
    for llave in da:
        unido[llave] = da[llave]
    for llave in db:
        unido[llave] = db[llave]

    return unido


def contar_letras(palabra):
    # Esta es otra manera de crear un diccionario vacio.
    # Es exactamente lo mismo que contadores = {}
    contadores = dict()

    for letra in palabra:

        # Si es primera vez que vemos la letra,
        # inicializamos su contador.
        if letra not in contadores:
            contadores[letra] = 0

        # Al llegar a este punto ya estamos seguros
        # que el contador existe, asi que simplemente
        # lo incrementamos en uno.
        contadores[letra] = contadores[letra] + 1

    return contadores


