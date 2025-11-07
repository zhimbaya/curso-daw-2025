# Entrada
n = int(raw_input('n: '))

# Proceso
c = 0
while n > 0:
    n = n / 10
    c = c + 1

# Salida
if c == 1:
    print '1 digito'
else:
    print c, 'digitos'

