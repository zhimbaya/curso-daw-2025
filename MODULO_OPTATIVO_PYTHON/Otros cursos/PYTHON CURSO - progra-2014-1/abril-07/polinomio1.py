# Solucion usando while con condicion.
# Se pregunta el coeficiente por primera
# vez afuera del ciclo, y despues al
# final de cada iteracion.

x = float(raw_input('x: '))

suma = 0.0
exp = 0

print 'Coeficientes:'
entrada = raw_input()
while entrada != 'FIN':
    a = float(entrada)
    suma += a * (x ** exp)
    exp += 1
    entrada = raw_input()

print 'p(x) =', suma




