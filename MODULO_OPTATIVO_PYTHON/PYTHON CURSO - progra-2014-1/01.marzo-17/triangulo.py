# Entrada
a = float(raw_input('Ingrese a: '))
b = float(raw_input('Ingrese b: '))
c = float(raw_input('Ingrese c: '))

# Proceso
if a == b == c:
    tipo = 'equilatero'
elif a == b or a == c or b == c:
    tipo = 'isoceles'
else:
    tipo = 'escaleno'

# Salida
print 'El triangulo es', tipo

