# Entrada
palabra = raw_input('Palabra: ')

# Proceso
n = len(palabra)
cuenta = 0
for i in range(n):
    letra = palabra[i]
    if letra in 'aeiou':
        cuenta += 1

# Salida
if cuenta == 1:
    print '1 vocal'
else:
    print cuenta, 'vocales'
