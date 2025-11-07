# Entrada
a = float(input('Ingrese a: '))
b = float(input('Ingrese b: '))
c = float(input('Ingrese c: '))

# Proceso
if a == b == c:
    tipo = 'equilatero'
elif a == b or a == c or b == c:
    tipo = 'isoceles'
else:
    tipo = 'escaleno'

# Salida
print('El triangulo es', tipo)

