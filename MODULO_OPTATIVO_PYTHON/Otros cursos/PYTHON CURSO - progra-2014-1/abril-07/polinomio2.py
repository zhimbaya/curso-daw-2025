# Solucion usando while infinito.
# Se pregunta el coeficiente al comenzar
# la iteracion, y si es 'FIN' se termina
# el ciclo de inmediato.

x = float(raw_input('x: '))

suma = 0.0
potencia = 1.0

print 'Coeficientes:'
while True:
    entrada = raw_input()
    if entrada == 'FIN':
        break
    a = float(entrada)
    suma += a * potencia
    potencia *= x

print 'p(x) =', suma




