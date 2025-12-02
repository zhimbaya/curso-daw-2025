# Entrada
n = int(raw_input('n: '))

# Proceso
es_primo = n > 1
for d in range(2, n):
    if n % d == 0:
        es_primo = False
        break

# Salida
if es_primo:
    print 'Primo'
else:
    print 'No primo'



