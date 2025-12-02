# Entrada
a = float(input('Primero: '))
b = float(input('Segundo: '))
c = float(input('Tercero: '))

# Proceso
if a <= b and a <= c:
    menor = a
    if b <= c:
        medio = b
        mayor = c
    else:
        medio = c
        mayor = b
elif b <= c:  # a ya no es el menor, solo comparar b y c
    menor = b
    if a <= c:
        medio = a
        mayor = c
    else:
        medio = c
        mayor = a
else: # ni a ni b son el menor, tiene que ser c
    menor = c
    if a <= b:
        medio = a
        mayor = b
    else:
        medio = b
        mayor = a

# Salida
print ('En orden:')
print (menor)
print (medio)
print (mayor)
