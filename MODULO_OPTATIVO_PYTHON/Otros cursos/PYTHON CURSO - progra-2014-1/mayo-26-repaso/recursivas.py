# Funciones recursivas son las que se llaman a si mismas.


# Que hace esta funcion?
def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x - 1)


# Que hace esta funcion?
def g(lista):
    if len(lista) == 0:
        return []
    else:
        cabeza = lista[0]
        cola = lista[1:]
        return [2 * cabeza] + g(cola)


# Que hace esta funcion?
def h(lista):
    if len(lista) == 0:
        return []
    m = min(lista)
    copia = list(lista)    # crea una copia de la lista
    copia.remove(m)
    return [m] + h(copia)

