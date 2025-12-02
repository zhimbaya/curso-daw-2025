def segundo(lista):
    return lista[1]

def divisores(n):
    d = []
    for i in range(1, n + 1):
        if n % i == 0:
            d.append(i)
    return d

def promedio(valores):
    # La funcion sum retorna la suma de los elementos de la lista.
    return float(sum(valores)) / len(valores)

def contar_mayores_que(m, lista):
    c = 0
    for x in lista:
        if x > m:
            c += 1
    return c

def emparejar(valores):
    parejas = []
    for i in range(len(valores) / 2):
        p = [valores[2 * i], valores[2 * i + 1]]
        parejas.append(p)
    return parejas

def emparejar2(valores):
    parejas = []
    p = []
    for x in valores:
        p.append(x)
        if len(p) == 2:
            parejas.append(p)
            p = []
    return parejas

def emparejar3(valores):
    n = len(valores)
    parejas = []
    for i in range(n / 2):
        # Aqui estoy usando el operador de rebanado.
        # Ver http://progra.usm.cl/apunte/materia/listas.html
        desde = 2 * i
        hasta  = 2 * i + 2
        parejas.append(valores[desde:hasta])
    return parejas


# Responder la pregunta del enunciado.
n = 142857
d = divisores(n)
c = contar_mayores_que(promedio(d), d)
print c, 'de los divisores de', n,
print 'son mayores que el promedio de todos ellos'

