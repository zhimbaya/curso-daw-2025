from math import sqrt

def promedio(valores):
    return float(sum(valores)) / len(valores)

def desviacion(valores):
    p = promedio(valores)
    s = 0.0
    for x in valores:
        s += (x - p) ** 2
    return sqrt(s / len(valores))

# Otra manera de calcular la desviacion:
# crear una lista con los cuadrados de las diferencias
# y obtener el promedio de ellas.
def desviacion2(valores):
    p = promedio(valores)
    diferencias = []
    for x in valores:
        diferencias.append((x - p) ** 2)
    return sqrt(promedio(diferencias))

def mediana(valores):
    # La funcion sorted retorna una nueva lista
    # que tiene los valores ordenados.
    # Es diferente de .sort(), que ordena la misma lista.
    ordenados = sorted(valores)
    n = len(valores)
    return ordenados[n / 2]


# Este if significa: ejecutar lo que sigue
# solo si se esta ejecutando datos.py como programa,
# no si se esta importando como modulo.
if __name__ == '__main__':

    n = int(raw_input('Cuantos datos? '))
    datos = []
    for i in range(n):
        x = float(raw_input('Dato ' + str(i + 1) + ': '))
        datos.append(x)

    print 'El promedio es', promedio(datos)
    print 'La desviacion estandar es', desviacion(datos)
    print 'La mediana es', mediana(datos)
