# Entrada
a = float(input('Primero: '))
b = float(input('Segundo: '))
c = float(input('Tercero: '))

menor = min(a, b, c)
mayor = max(a, b, c)
medio = a + b + c - menor - mayor

print('En orden descendente:')
print(menor)
print(medio)
print(mayor)
