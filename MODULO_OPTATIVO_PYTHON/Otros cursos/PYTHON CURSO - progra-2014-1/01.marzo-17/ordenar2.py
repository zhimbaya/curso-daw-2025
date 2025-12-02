# Entrada
a = float(raw_input('Primero: '))
b = float(raw_input('Segundo: '))
c = float(raw_input('Tercero: '))

menor = min(a, b, c)
mayor = max(a, b, c)
medio = a + b + c - menor - mayor

print 'En orden:'
print menor
print medio
print mayor
